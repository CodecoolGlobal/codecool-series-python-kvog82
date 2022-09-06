from data import data_manager
from psycopg2 import sql


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows ORDER BY title;')


def get_shows_by_rating():
    return data_manager.execute_select("""
    SELECT shows.id, 
            title, 
            date_part('year', year) AS year, 
            runtime, 
            ROUND(rating, 1) as rating,
            STRING_AGG(g.name, ', ' ORDER BY g.name) AS genre, 
            trailer, 
            homepage
    FROM shows
    LEFT JOIN show_genres sg on shows.id = sg.show_id
    LEFT JOIN genres g on g.id = sg.genre_id
    GROUP BY shows.id, title, year, runtime, ROUND(rating, 1), trailer, homepage
    ORDER BY rating DESC
    """)


def get_most_rated_shows(order_by, order_direction, limit, offset):
    return data_manager.execute_select(sql.SQL("""
    SELECT shows.id, 
            title, 
            date_part('year', year) AS year, 
            runtime, 
            ROUND(rating, 1) as rating, 
            STRING_AGG(g.name, ', ' ORDER BY g.name) AS genre , 
            trailer, 
            homepage
    FROM shows
    LEFT JOIN show_genres sg on shows.id = sg.show_id
    LEFT JOIN genres g on g.id = sg.genre_id
    GROUP BY shows.id, title, year, runtime, ROUND(rating, 1), trailer, homepage
    ORDER BY {order_by} {order_direction}
    LIMIT %(limit)s OFFSET %(offset)s
    """).format(order_by=sql.Identifier(order_by),
                order_direction=sql.SQL(order_direction),
                limit=sql.Identifier(str(limit)),
                offset=sql.Identifier(str(offset))), variables= {'limit': limit, 'offset': offset})


def get_show_details(show_id):
    return data_manager.execute_select("""
    SELECT title, 
           runtime, 
           ROUND(rating, 1) as rating, 
           STRING_AGG(g.name, ', ' ORDER BY g.name) AS genres,
           trailer,
           overview
    FROM shows
    LEFT JOIN show_genres sg on shows.id = sg.show_id
    LEFT JOIN genres g on sg.genre_id = g.id
    WHERE shows.id = %(id)s
    GROUP BY title, runtime, rating, trailer, overview
    """, variables={'id': show_id})


def get_show_actors(show_id):
    return data_manager.execute_select("""
    SELECT a.name
    FROM shows
    LEFT JOIN show_characters sc on shows.id = sc.show_id
    LEFT JOIN actors a on sc.actor_id = a.id
    WHERE shows.id = %(id)s
    LIMIT 3
    """, variables={'id': show_id})


def get_show_seasons(show_id):
    return data_manager.execute_select("""
    SELECT seasons.season_number, seasons.title, seasons.overview
    FROM seasons
    LEFT JOIN shows s on seasons.show_id = s.id
    WHERE s.id = %(id)s
    ORDER BY seasons.season_number
    """, variables={'id': show_id})


def get_first_hundred_actors():
    return data_manager.execute_select("""
    SELECT *
    FROM (
        SELECT name, birthday
        FROM actors
        LIMIT 100) as actors
    ORDER BY birthday DESC;
    """)


def get_actors_shows(actor_name):
    return data_manager.execute_select("""
    SELECT shows.title
    FROM shows
    LEFT JOIN show_characters sc on shows.id = sc.show_id
    LEFT JOIN actors a on sc.actor_id = a.id
    WHERE a.name = %(actor_name)s
    """, variables={'actor_name': actor_name})


def get_shows_ratings():
    return data_manager.execute_select("""
        SELECT shows.title,
                ROUND(shows.rating - (
                (SELECT AVG(rating)
                FROM shows)), 3) AS rating
        FROM shows
        LEFT JOIN show_characters sc on shows.id = sc.show_id
        LEFT JOIN actors a on sc.actor_id = a.id
        GROUP BY shows.title, rating
        ORDER BY COUNT(a.name) DESC , rating DESC
        LIMIT 10
    """)


def get_ordered_shows_by_episode_count(order_direction):
    return data_manager.execute_select(sql.SQL("""
        SELECT shows.title,
            ROUND(rating) as rating
            FROM shows
            LEFT JOIN seasons s on shows.id = s.show_id
            LEFT JOIN episodes e on s.id = e.season_id
            GROUP BY shows.title, ROUND(rating)
            ORDER BY COUNT(e.id) {order_direction}
            LIMIT 10
        """).format(order_direction=sql.SQL(order_direction)))


def get_genres():
    return data_manager.execute_select("""
    SELECT name
    FROM genres
    ORDER BY name
    """)


def get_actors_by_genre(genre):
    return data_manager.execute_select("""
        SELECT actors.name
        FROM actors
        LEFT JOIN show_characters sc on actors.id = sc.actor_id
        LEFT JOIN show_genres sg on sc.show_id = sg.show_id
        LEFT JOIN genres g on g.id = sg.genre_id
        WHERE g.name = %(genre)s
        LIMIT 20
    """, variables={'genre': genre})


def get_actors_by_genre_and_character(genre, character):
    return data_manager.execute_select("""
        SELECT actors.name
        FROM actors
        LEFT JOIN show_characters sc on actors.id = sc.actor_id
        LEFT JOIN show_genres sg on sc.show_id = sg.show_id
        LEFT JOIN genres g on g.id = sg.genre_id
        WHERE g.name = %(genre)s AND
          sc.character_name ILIKE %(character)s
        LIMIT 20
    """, variables={'genre': genre, 'character': '%' + character + '%'})


def get_first_hundred_alive_actors():
    return data_manager.execute_select("""
    SELECT name, 
            birthday,
            CAST(EXTRACT(day from birthday) AS INTEGER) AS day
    FROM actors
    WHERE death is null
    ORDER BY birthday
    LIMIT 100
    """)
