from abc import ABCMeta , abstractmethod

from the_finder.contracts.IntefaceApi import InterfaceApi
from the_finder.models.Search import Search
from the_finder.tasks import search_files

class TheFinderApi(InterfaceApi):
    
    def create_search(search_params :dict) -> str:
        new_search = Search(**search_params)
        new_search.save()
        search_files.delay(new_search.pk)
        return new_search.pk
    
    def get_result(search_key :str) -> dict:
        return Search.get(search_key).search_res