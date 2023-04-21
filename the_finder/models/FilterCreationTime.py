from os.path import getctime
from datetime import datetime
from zipfile import ZipInfo

from pydantic import StrictFloat , validator, StrictStr
from the_finder.models.Filter import Filter


class FilterCreationTime(Filter):
    value : StrictStr
    timestamp : StrictFloat = 0
    
    @validator('timestamp', pre=True , always=True)
    def set_timestamp_value(cls,v,values):
        if 'value' in values:
            try:
                v = datetime.fromisoformat(values['value'].upper().replace("Z", "+00:00")).timestamp()
            except ValueError as e:
                raise ValueError('creation_time.value must be correct ISO 8601 datetime')
        return v
    
    def get_value(self) -> float:
        return self.timestamp

    def chek_compilance(self, fpath: str) -> bool:
        return self._comparate(getctime(fpath))

    def chek_arhive_compilance(self, z_info: ZipInfo) -> bool:
        return self._comparate(datetime(*z_info.date_time).timestamp())
