import redis
from flask import Flask
from redis_om import Migrator

app = Flask(__name__)
import the_finder.config

redis_client = redis.Redis(
    host=app.config["REDIS_HOST"], 
    port=app.config["REDIS_PORT"], 
    db=app.config["REDIS_DB_NUM"])

import the_finder.tasks
import the_finder.routes

Migrator().run()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')