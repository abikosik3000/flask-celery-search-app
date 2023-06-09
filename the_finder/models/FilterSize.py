from os.path import getsize
from zipfile import ZipInfo

from redis_om import Field
from pydantic import validator, StrictInt
from the_finder.models.Filter import Filter


class FilterSize(Filter):
    value : StrictInt
    
    def get_value(self) -> int:
        return int(self.value)

    def chek_compilance(self, fpath: str) -> bool:
        return self._comparate(getsize(fpath))

    def chek_arhive_compilance(self, z_info: ZipInfo) -> bool:
        return self._comparate(z_info.file_size)
