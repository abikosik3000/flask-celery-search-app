from redis_om import Migrator
from flask import request

from the_finder import app
from the_finder.controllers.SearchController import SearchController


@app.route("/")
def get_main():
    return "main"


@app.route("/search", methods=["POST", "GET"])
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


@app.route("/shutdown", methods=["GET"])
def shutdown():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()
    return "Server shutting down..."
