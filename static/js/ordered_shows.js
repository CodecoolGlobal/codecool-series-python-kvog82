const tableBody = document.querySelectorAll('.ordered-shows')[0];
const sortColumn = document.getElementsByClassName('action-column')[0];

sortColumn.addEventListener('click', orderShows);


async function orderShows() {
    let params = new URLSearchParams;
    if (sortColumn.classList.contains('desc')) {
        params.set('order_direction', 'desc');
        sortColumn.classList.replace('desc', 'asc')
    } else {
        params.set('order_direction', 'asc');
        sortColumn.classList.replace('asc', 'desc')
    }

    let response = await fetch('/api/ordered-shows?' + params.toString())
    let orderedShows = await response.json();

    tableBody.innerHTML = displayOrderedShows(orderedShows);
}


function displayOrderedShows(orderedShows) {
    let bodyHtml = ``
    for (let show of orderedShows) {
        let rating = convertRating(show.rating);
        bodyHtml += `
        <tr>
            <td>${show.title}</td>
            <td>${rating}</td>
        </tr>
        `
    }

    return bodyHtml;
}


function convertRating(rating) {
    let ratingStars = ''
    for (let i=0; i<rating; i++) {
        ratingStars += '★'
    }
    return ratingStars;
}

orderShows();