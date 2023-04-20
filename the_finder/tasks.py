from . import make_celery

celery = make_celery()

@celery.task
def test():
    from the_finder.models.Search import Search
    print(Search.get("01GYFHGTC3N60ND9W1M3WFMH04").search_res)
    