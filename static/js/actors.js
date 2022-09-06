let actors = document.querySelectorAll('.actor')

for (let i=0; i<actors.length; i++) {
    actors[i].addEventListener('click', getActorsShows)
}

async function getActorsShows(event) {
    let actor = event.currentTarget;

    if (actor.classList.contains('active')) {
        actor.classList.remove('active');
        actor.removeChild(actor.children[0]);
    } else {
        for (let i = 0; i < actors.length; i++) {
            actors[i].classList.remove('active')
            if (actors[i].children.length > 0) {
                actors[i].removeChild(actors[i].children[0]);
            }
        }

        actor.classList.add('active')
        let actorName = actor.innerText;

        let params = new URLSearchParams;
        params.set('actor_name', actorName)

        let response = await fetch('/api/actors-shows?' + params.toString())
        let actorsShows = await response.json()
        actor.innerHTML += await addShows(actorName, actorsShows);
    }
}

async function addShows(actorName, actorsShows) {
    let showsList = '';
    if (actorsShows.length === 0) {
        showsList = `
            <ul class="shows-list">
                <li>no Shows</li>
            </ul>
        `
    } else {
        showsList = `
            <ul class="shows-list">
        `

        for (let show of actorsShows) {
            showsList += `
                <li>${show.title}</li>
            `
            }

        showsList += `
            </ul>
        `
    }
    return showsList;
}