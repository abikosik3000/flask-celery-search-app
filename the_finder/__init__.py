import redis
from flask import Flask
from redis_om import Migrator


app = Flask(__name__)
import the_finder.config

redis_client = redis.Redis(
    host=app.config["REDIS_PORT"],
    port=app.config["REDIS_HOST"], 
    db=app.config["REDIS_DB_NUM"],
    
    )

import the_finder.tasks
import the_finder.routes


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')