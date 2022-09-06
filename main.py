from flask import Flask, render_template, url_for, jsonify, request
from data import queries
import math
from dotenv import load_dotenv

SHOWS_ON_PAGE = 15

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('util-design.html')


@app.route('/shows/most-rated/', methods=['GET'])
def shows_most_rated():
    number_of_pages = math.ceil(len(queries.get_shows()) / SHOWS_ON_PAGE)
    current_page = 1
    order_by = 'rating'
    order_direction = 'desc'
    offset = (current_page-1)*SHOWS_ON_PAGE+1
    shows_most_rated = queries.get_most_rated_shows(order_by=order_by, order_direction=order_direction,
                                                    limit=SHOWS_ON_PAGE, offset=offset)
    return render_template('shows-most-rated.html', shows_most_rated=shows_most_rated,
                           current_page=current_page, number_of_pages=number_of_pages)


@app.route('/api/shows/pagination')
def api_shows_pagination():
    page = request.args['page_index']
    order_by = request.args['order_by']
    order_direction = request.args['order_direction']
    current_page = int(page)
    offset = (current_page - 1) * SHOWS_ON_PAGE + 1
    shows = queries.get_most_rated_shows(order_by=order_by, order_direction=order_direction,
                                 limit=SHOWS_ON_PAGE, offset=offset)
    return jsonify(shows)


@app.route('/api/shows/sorting')
def api_shows_sorting():
    order_by = request.args['order_by']
    order_direction = request.args['order_direction']
    page = 1
    offset = (page - 1) * SHOWS_ON_PAGE + 1
    ordered_shows = queries.get_most_rated_shows(order_by=order_by,
                    order_direction=order_direction, limit=SHOWS_ON_PAGE, offset=offset)
    return jsonify(ordered_shows)


@app.route('/show/<id>')
def show_details(id):
    show_details = queries.get_show_details(id)
    actors = queries.get_show_actors(id)

    runtime_minutes = show_details[0].get('runtime')
    hours = runtime_minutes // 60
    minutes = runtime_minutes % 60
    if hours and minutes:
        runtime_new = '{}h {}min'.format(hours, minutes)
    elif hours and not minutes:
        runtime_new = '{}h'.format(hours)
    elif minutes and not hours:
        runtime_new = '{}min'.format(minutes)

    show_details[0]['runtime'] = runtime_new

    trailer = show_details[0].get('trailer')
    if trailer:
        video_id = trailer.split('=')[1]
        show_details[0]['trailer'] = video_id

    show_actors = []
    for actor in actors:
        show_actors.append(actor['name'])

    show_seasons = queries.get_show_seasons(id)

    return render_template('show-details.html', show_details=show_details,
                           show_actors=show_actors, show_seasons=show_seasons)


@app.route('/actors')
def actors():
    actors = queries.get_first_hundred_actors()
    return render_template('actors.html', actors=actors)


@app.route('/api/actors-shows')
def api_actors_shows():
    actor_name = request.args['actor_name']
    actors_shows = queries.get_actors_shows(actor_name)
    return jsonify(actors_shows)


@app.route('/ratings')
def ratings():
    shows_with_ratings = queries.get_shows_ratings()
    return render_template('ratings.html', shows_with_ratings=shows_with_ratings)


@app.route('/ordered-shows')
def ordered_shows():
    return render_template('ordered-shows.html')


@app.route('/api/ordered-shows')
def api_ordered_shows():
    order_direction = request.args['order_direction']
    ordered_shows = queries.get_ordered_shows_by_episode_count(order_direction)
    return jsonify(ordered_shows)


@app.route('/filter-actors')
def filter_actors():
    genres = queries.get_genres()
    return render_template('filter-actors.html', genres=genres)


@app.route('/api/filter-actors')
def api_filter_actors():
    genre = request.args['genre']
    character = request.args['character']
    actors = queries.get_actors_by_genre(genre)
    if character:
        actors = queries.get_actors_by_genre_and_character(genre, character)
    return jsonify(actors)


@app.route('/birthday-actors')
def birthday_actors():
    return render_template('birthday-actors.html', actors=actors)


@app.route('/api/birthday-actors')
def api_birthday_actors():
    actors = queries.get_first_hundred_alive_actors()
    return jsonify(actors)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
