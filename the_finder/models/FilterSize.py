from the_finder.models.Filter import Filter

class FilterSize(Filter):
    def chek_compilance(self, fpath: str) -> bool:
        return True