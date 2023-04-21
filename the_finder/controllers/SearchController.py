import json

from flask import request , jsonify
from pydantic import ValidationError
from redis_om import NotFoundError

from the_finder.controllers.Controller import Controller
from the_finder.services.TheFinderApi import TheFinderApi


class SearchController(Controller):
    @staticmethod
    def post_search(request):
        try:
            search_key = TheFinderApi.create_search(request.get_json())
            return jsonify({'search_key': search_key}), 200
        except ValidationError as e:
            return jsonify(e.errors()), 400
        
    @staticmethod
    def get_searches(request,search_key):
        try:
            result = TheFinderApi.get_result(search_key)
            return jsonify(result), 200
        except NotFoundError as e:
            return jsonify({'error' : 'search id not found'}), 400
        