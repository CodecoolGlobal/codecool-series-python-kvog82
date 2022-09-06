let container = document.getElementsByClassName('actors')[0];

async function getActors() {
    let response = await fetch('/api/birthday-actors');
    return await response.json();
}

async function generateActorsList() {
    let actors = await getActors();
    let containerBody = ''
    actors.forEach(function(actor) {

        containerBody += `
        <li class="actor">${actor.name}
            <span class="invisible ${getBackgroundClass(actor.day)}">
                ${convertDate(actor.birthday)}
            </span>
        </li>
        `
    })

    function getBackgroundClass(day) {
        let backgroundColor = 'grey'
        if (day % 2 === 0) {
            backgroundColor = 'green';
        }
        return backgroundColor
    }

    function convertDate(date) {
         return date.toString().substring(0,17);
    }

    container.innerHTML = containerBody;
}

async function main() {
    await generateActorsList();
    let listItems = document.getElementsByClassName('actor');
    for (let i=0; i<listItems.length; i++) {
        listItems[i].addEventListener('mouseover', function () {
            listItems[i].children[0].classList.remove('invisible');
        })
        listItems[i].addEventListener('mouseout', function () {
            listItems[i].children[0].classList.add('invisible');
        })
    }
}

main();