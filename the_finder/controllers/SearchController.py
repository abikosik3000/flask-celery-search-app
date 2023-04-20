import json

from flask import request , jsonify

from the_finder.controllers.Controller import Controller
from the_finder.models.Search import Search
from the_finder.tasks import search_files

class SearchController(Controller):
    test_s = '{\
                "text": "th",\
                "file_mask": "*",\
                "size": {\
                    "value": 0,\
                    "operator": "gt"\
                },\
                "creation_time": {\
                    "value": "2020-03-03T14:00:54Z",\
                    "operator": "gt"\
                }\
            }'

    @staticmethod
    def post_search(request):
        #req_data = request.get_json()
        new_search = Search(**json.loads(SearchController.test_s))#req_data
        new_search.save()
        search_files.delay(new_search.pk)
        #new_search.search()
        return jsonify({'search_key': new_search.pk}) ,200

    @staticmethod
    def get_searches(request,search_id):
        now_search = Search.get(search_id).search_res
        return jsonify(now_search) ,200