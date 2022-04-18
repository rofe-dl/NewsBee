# NewsBee
NewsBee is a country-based news sharing website written in Python backed by Django and the Mediastack API for retrieving news. Users register with their country and login. Home page is divided into 3 sections
1. **News**, where users sees news from their own country
1. **BeeNews**, where users see news shared by other users
1. **My Collection**, where users see the news they shared

[Sign up and get a Mediastack API key here](https://mediastack.com/)

1. Install MariaDB and the required development libraries for it
    ```
    // Development libraries
    sudo apt install libmariadb-dev libmariadb-dev-compat libmariadbclient-dev
    sudo apt install python3-dev
    ```
1. Create a database called `news_bee` in MariaDB
1. In the `NewsBee` directory, make a `secrets.py` file and write down the secret variables required
    ```
    DJANGO_SECRET_KEY = '<any random string>'
    DATABASE_PASSWORD = '<your mariadb database password>'
    MEDIASTACK_KEY = '<your api key>'
    ```
    Then in the `settings.py` file, search for `DATABASES` and change the username there to the username of your database (usually `root`)
1. Make a virtual environment of python and install dependencies
    ```
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

1. Migrate the changes to your database.

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate 
    ```
1. Run the server with `python3 manage.py runserver`