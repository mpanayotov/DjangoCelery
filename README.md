Using Celery to illustrate the difference in execution times of Synchronous and Asynchronous Tasks.

using redis as a Broker

#to install requirements for project
pip install -r requirements.txt

#to run celery
celery -A DjangoCelery worker --logleve=info

#to run django
python manage.py runserver
