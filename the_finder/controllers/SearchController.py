import json

from flask import request , jsonify
from pydantic import ValidationError
from redis_om import NotFoundError

from the_finder.controllers.Controller import Controller
from the_finder.services.TheFinderApi import TheFinderApi


class SearchController(Controller):
    test_s = '{\
                "text": "th",\
                "file_mask": "*",\
                "size": {\
                    "value": 1,\
                    "operator": "gt"\
                },\
                "creation_time": {\
                    "value": "2020-03-03T14:00:54Z",\
                    "operator": "gt"\
                }\
            }'

    @staticmethod
    def post_search(request):
        try:
            json_dict = json.loads(SearchController.test_s) #request.get_json()
            search_key = TheFinderApi.create_search(json_dict)
            return jsonify({'search_key': search_key}), 200
        except ValidationError as e:
            return e.json(), 400
        
    @staticmethod
    def get_searches(request,search_key):
        try:
            result = TheFinderApi.get_result(search_key)
            return jsonify(result), 200
        except NotFoundError as e:
            return "this ID was not found", 400
        