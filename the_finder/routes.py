from redis_om import Migrator
from flask import request, abort

from the_finder import app
from the_finder.controllers.SearchController import SearchController


@app.route("/search", methods=["POST"])
def search():
    return SearchController.post_search(request)


@app.route("/searches/<string:search_id>", methods=["GET"])
def searches(search_id):
    return SearchController.get_searches(request, search_id)


"""
OTHER PATH
"""


@app.route("/migrate", methods=["GET"])
def migrate():
    Migrator().run()
    return "Migrating..."
