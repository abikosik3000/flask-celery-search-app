import os

from the_finder import app

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["BASEDIR"] = basedir

#Директория для поиска файлов
app.config["SEARCH_DIRECTORY"] = "/home/abikosik3000/var/www/search_app/test_repo"

#REDIS
app.config["REDIS_HOST"] = '6379'
app.config["REDIS_PORT"] = '6379'
app.config["REDIS_DB_NUM"] = '0'
app.config["REDIS_USER"] = None
app.config["REDIS_PASS"] = None

#CELERY
app.config["CELERY_BROKER"] = "redis://localhost"
app.config["CELERY_BACKEND"] = None


