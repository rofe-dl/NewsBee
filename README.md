# NewsBee
NewsBee is a country-based news sharing website written in Python backed by Django and the Mediastack API for retrieving news. Users register with their country and login. Home page is divided into 3 sections
1. **News**, where users sees news from their own country
1. **BeeNews**, where users see news shared by other users
1. **My Collection**, where users see the news they shared


**Please install the packages in requirements.txt (in your virtual environment preferably) and create a database in your MySQL called "news_bee". Change the database details in NewsBee/settings.py according to your database configuration.**

To start the website, go to the command line and switch to your python virtual environment if you installed the packages in one. Then run:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


**If you're on a Linux system, then use python3 instead of just python**