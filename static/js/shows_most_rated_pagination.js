import {displayShows} from "./shows_most_rated_display_shows.js";

export const pages = document.getElementsByClassName('pagination')[0].children;

for (let i=0; i < pages.length; i++) {
    let page = pages[i];
    pages[1].classList.add('active-page');
    page.addEventListener('click', selectPage)
}

async function selectPage(event) {
    let actionColumn = document.getElementsByClassName('action-column')[0]
    let currentPage = document.getElementsByClassName('active-page')[0].innerText;

    for (let i=0; i < pages.length; i++) {
    let page = pages[i];
    page.classList.remove('active-page')
    }
    event.currentTarget.classList.add('active-page')

    let pageIndex = event.currentTarget.innerText;
    if (pageIndex ==='<<') {
        pageIndex = handlePageDown(currentPage, event.currentTarget);
    }

    if (pageIndex ==='>>') {
        console.log(currentPage)
        pageIndex = handlePageUp(currentPage, event.currentTarget);
    }

    let orderBy = actionColumn.id;
    let orderDirection = 'desc';
    if (actionColumn.classList.contains('asc')) {
        orderDirection = 'asc';
    }

    let params = new URLSearchParams;
    params.set('page_index', pageIndex)
    params.set('order_by', orderBy)
    params.set('order_direction', orderDirection)

    let url = '/api/shows/pagination?'

    let response = await fetch(url + params.toString());
    let showsOnPage = await response.json();

    displayShows(showsOnPage);
}

function handlePageDown(currentPage, target) {
    let pageDown;
    if (currentPage > 1) {
        pageDown = parseInt(currentPage) - 1;
        target.classList.remove('active-page')
        pages[currentPage-1].classList.add('active-page')
    } else {
        pageDown = 1;
        target.classList.remove('active-page')
        pages[1].classList.add('active-page')
    }
    return pageDown;
}

function handlePageUp(currentPage, target) {
    let pageUp;
    currentPage = parseInt(currentPage);
    if (currentPage < 68) {
        pageUp = currentPage + 1;
        target.classList.remove('active-page')
        pages[pageUp].classList.add('active-page')
    } else {
        pageUp = 68;
        target.classList.remove('active-page')
        pages[pageUp].classList.add('active-page')
    }
    return pageUp;
}