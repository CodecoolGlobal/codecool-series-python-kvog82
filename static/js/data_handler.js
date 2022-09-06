export async function getShowsMostRated (pageIndex) {
    return await getData(`/api/shows/most-rated/${pageIndex}`);
}

export async function getAllShows() {
    return await getData('/api/all-shows');
}

async function getData(url) {
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.ok) {
        return await response.json();
    }
}

export async function getShowsSorted(url, params) {
    let response = await fetch(url + params.toString())
    return await response.json()
}