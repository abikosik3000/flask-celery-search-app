from the_finder.celery import celery
from the_finder.models.Search import Search


@celery.task
def search_files(search_id :str):
    '''celeru task performing a file search'''
    Search.get(search_id).search()
    