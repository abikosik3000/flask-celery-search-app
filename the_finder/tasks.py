from . import make_celery

celery = make_celery()

@celery.task
def test():
    print('s')
    