from celery import Celery

from the_finder import app


def make_celery(app):
    '''creates celery compatible with flask,
    using flask config
    '''
    
    celery = Celery(
        broker=app.config["CELERY_BROKER"],
        include="the_finder.tasks",
        task_ignore_result=True,
    )

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)

if __name__ == "__main__":
    celery.start()