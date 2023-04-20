from the_finder.controllers.Controller import Controller
from the_finder.models.Search import Search
from flask import request , jsonify
import json

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
#Z
    @staticmethod
    def post_search(request):
        #req_data = request.get_json()
        new_search = Search(**json.loads(SearchController.test_s))#req_data
        new_search.save()
        new_search.search()
        return jsonify(new_search.search_res)
        #return jsonify({'search_key': new_search.pk}) ,200

    @staticmethod
    def get_searches(request,search_id):
        now_search = Search.get(search_id).search_res
        return jsonify(now_search) ,200