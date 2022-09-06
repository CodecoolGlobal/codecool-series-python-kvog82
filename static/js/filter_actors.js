const genres = document.getElementById('genre');
const characters = document.querySelectorAll('.character')[0];
const actorsList = document.getElementById('actors-result');

genres.addEventListener('change', getActorsByGenre);
characters.addEventListener('input', getActorsByGenre);

async function getActorsByGenre(event) {
    actorsList.innerHTML = '';

    let genre = (genres.options[genres.selectedIndex].value);
    let character = characters.value;

    let params = new URLSearchParams;
    params.set('genre', genre)
    params.set('character', character)

    let response = await fetch('/api/filter-actors?' + params.toString());
    let actors = await response.json();

    for (let actor of actors) {
        actorsList.innerHTML += `<div>${actor.name}</div>`;
    }
}


getActorsByGenre();