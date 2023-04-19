from the_finder.models.Filter import Filter

class FilterCreationTime(Filter):
    def chek_compilance(self, fpath: str) -> bool:
        return True