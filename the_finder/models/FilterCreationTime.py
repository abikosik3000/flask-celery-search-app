from the_finder.models.Filter import Filter
from os.path import getctime
from datetime import datetime

class FilterCreationTime(Filter):

    def get_value(self) -> float:
        return datetime.fromisoformat(self.value.replace('Z','+00:00')).timestamp()
    
    def chek_compilance(self, fpath: str) -> bool:
        return self._comparate(getctime(fpath))