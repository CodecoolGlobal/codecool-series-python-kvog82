# Codecool series

Codecool series is a solo project from the web module (second module) in the Codecool curriculum.

It is a website where users can find their favorite TV shows. The database contains information for more than 1000 
shows that can be sorted by various parameters (e.g. title, year or ratings) or be found by actor, genre or character.

## Technologies used

HTML/Jinja2, JavaScript, Python, Flask, PostgreSQL 

### Focus
* PostgreSQL queries with SELECT, WHERE, JOIN, GROUP BY, ORDER BY, LIMIT, OFFSET and aggregate functions
* Flask routes and variable rules
* Jinja2 templating
* some JavaScript

## How to run this application

Open Terminal and clone the project
```ssh
git clone git@github.com:CodecoolGlobal/codecool-series-python-kvog82.git
```

Go to the project directory
```ssh
cd codecool-series-python-kvog82
```

Create virtualenv
```ssh
virtualenv -p python3 venv
```

Enter venv
```ssh
source venv/bin/activate
```

Install requirements
```ssh
pip install -r requirements.txt
```

#### Setup the database
Create a PostgreSQL database and set environmental variables by making a copy of .env.template named `.env` and 
filling in the details.
* MY_PSQL_DBNAME – The name of the database
* MY_PSQL_HOST – localhost
* MY_PSQL_USER
* MY_PSQL_PASSWORD – The database user password (if no password is needed, put a random word here)
* TRAKT_API_KEY – You can leave this empty

Run `data/data_inserter.py` from PyCharm to create your database.

#### Start the application
Run main.py
```ssh
python3 main.py
```

Now you can watch the website at the following URL: http://127.0.0.1:5000/

## Screenshots
Front page
![cc-series_01_frontpage](https://user-images.githubusercontent.com/102434853/230028537-e99fad27-33c5-409c-90f8-1ebb5322d079.png)

Shows
![cc-series_02_shows](https://user-images.githubusercontent.com/102434853/230028705-5f04b202-9567-48eb-afb1-ff84794def85.png)

Show details
![cc-series_03_show-details](https://user-images.githubusercontent.com/102434853/230028752-79ab3d76-87fb-4e5d-a5bf-e227d256a6e4.png)