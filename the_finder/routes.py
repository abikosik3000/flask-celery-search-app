from redis_om import Migrator
from flask import request, abort

from the_finder import app
from the_finder.controllers.SearchController import SearchController


@app.route("/search", methods=["POST"])
def search():
    '''start search files'''
    return SearchController.post_search(request)


@app.route("/searches/<string:search_id>", methods=["GET"])
def searches(search_id):
    '''return search status and results'''
    return SearchController.get_searches(request, search_id)

# other paths

@app.route("/migrate", methods=["GET"])
def migrate():
    '''migrating models'''
    Migrator().run()
    return "Migrating..."
