#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)
import the_finder.config

#------------------------
from celery import Celery, Task

CELERY_TASK_LIST = [
    'the_finder.tasks'
]

def make_celery():
    celery = Celery(
        broker="redis://localhost",
        backend="redis://localhost",
        include=CELERY_TASK_LIST
    )

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self,*args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self,*args, **kwargs )
            
    celery.Task = ContextTask
    return celery

#--------------------
import the_finder.routes


@app.route('/test')
def index():
    from the_finder.tasks import test
    test.delay()
    #async_function.delay(1, 2)
    return 'Task has been submitted '


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')