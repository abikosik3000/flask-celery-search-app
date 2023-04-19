from the_finder.models.Filter import Filter
from os.path import getsize

class FilterSize(Filter):

    def get_value(self) -> int:
        return int(self.value)

    def chek_compilance(self, fpath: str) -> bool:
        return self._comparate(getsize(fpath))