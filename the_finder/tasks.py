from .celery import celery
from the_finder.models.Search import Search

@celery.task
def test():
    s = 0
    for i in range(1000000):
        s = 0 + 1
    print(Search.get("01GYFZEEV3TTY5SH5RMXSB58K2").search_res)
    