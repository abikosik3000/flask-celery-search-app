from os.path import getctime
from datetime import datetime
from zipfile import ZipInfo

from the_finder.models.Filter import Filter


class FilterCreationTime(Filter):
    def get_value(self) -> float:
        return datetime.fromisoformat(self.value.replace("Z", "+00:00")).timestamp()

    def chek_compilance(self, fpath: str) -> bool:
        return self._comparate(getctime(fpath))

    def chek_arhive_compilance(self, z_info: ZipInfo) -> bool:
        return self._comparate(datetime(*z_info.date_time).timestamp())
