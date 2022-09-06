import {getShowsSorted} from "./data_handler.js";
import {displayShows} from "./shows_most_rated_display_shows.js";
import {pages} from "./shows_most_rated_pagination.js";

const sortingColumns = document.querySelectorAll('.sort-column')
    for (let i=0; i < sortingColumns.length; i++) {
    sortingColumns[i].addEventListener('click', sortColumns);
    }

async function sortColumns(event) {
    let orderBy = event.currentTarget.id;
    let orderDirection = 'asc';
    if (orderBy === 'title' || orderBy === 'runtime') {
        orderDirection = 'asc';
        if (event.currentTarget.classList.contains('asc')) {
                orderDirection = 'desc';
        }
    }

    if (orderBy === 'year' || orderBy === 'rating') {
        orderDirection = 'desc';
        if (event.currentTarget.classList.contains('desc')) {
                orderDirection = 'asc';
        }
    }

    for (let i=0; i < sortingColumns.length; i++) {
    sortingColumns[i].classList.remove('action-column');
    sortingColumns[i].classList.remove('desc');
    sortingColumns[i].classList.remove('asc');
    }

    event.currentTarget.classList.add('action-column');
    event.currentTarget.classList.add(orderDirection);

    let params = new URLSearchParams;
    params.set('order_by', orderBy)
    params.set('order_direction', orderDirection)

    for (let i=0; i < pages.length; i++) {
    let page = pages[i];
    page.classList.remove('active-page')
    }
    pages[1].classList.add('active-page')

    let sortedShows = await getShowsSorted('/api/shows/sorting?', params.toString())
    displayShows(sortedShows);
}