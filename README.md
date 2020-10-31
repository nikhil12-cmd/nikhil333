# nikhil333
 git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
Your app should now be running on localhost:5000.

heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
