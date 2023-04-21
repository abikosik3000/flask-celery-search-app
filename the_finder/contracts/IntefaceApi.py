from abc import ABCMeta , abstractstaticmethod

class InterfaceApi(ABCMeta):
    @abstractstaticmethod
    def create_search(search_params :dict) -> str:
        pass

    @abstractstaticmethod
    def get_result(search_key :str) -> dict:
        pass