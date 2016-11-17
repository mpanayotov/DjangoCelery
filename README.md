Using Celery to illustrate the difference in execution times of Synchronous and Asynchronous Tasks.

using redis as a Broker

commands:
	pip install -r requirements.txt
	celery -A DjangoCelery worker --logleve=info
