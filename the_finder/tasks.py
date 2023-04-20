from the_finder.celery import celery
from the_finder.models.Search import Search


@celery.task
def search_files(search_id :str):
    Search.get(search_id).search()
    