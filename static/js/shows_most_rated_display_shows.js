export function displayShows(sorted_Shows) {
    let tableBody = document.getElementsByClassName('shows-most-rated');
    tableBody[0].innerHTML = '';
    let newTableBody = '';
    for (let show of sorted_Shows) {
        newTableBody += `
            <tr>
            <td><a href="/show/${ show.id }">${ show.title }</a></td>
            <td>${ show.year }</td>
            <td>${ show.runtime }</td>
            <td>${ show.rating }</td>
            <td>${ show.genre }</td>`

            if (show.trailer) {
                newTableBody += `<td><a href="${ show.trailer }" target="_blank">${ show.trailer }</a></td>`
            } else {
                newTableBody += `<td>no URL</td>`
            }

            if (show.homepage) {
                newTableBody += `<td><a href="${ show.homepage }" target="_blank">${ show.homepage }</a></td></tr>`
            } else {
                newTableBody += `<td>no URL</td></tr>`
            }
    }
    tableBody[0].innerHTML = newTableBody;
}