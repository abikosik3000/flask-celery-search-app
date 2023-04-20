from abc import ABC , abstractmethod
from zipfile import ZipInfo

from redis_om import EmbeddedJsonModel, Field


class Filter(EmbeddedJsonModel,ABC):
    value: str = Field(index=True)
    operator: str = Field(index=True)

    def get_value(self):
        return self.value

    def _comparate(self, x) -> bool:
        y = self.get_value()
        match self.operator:
            case "eq": 
                return x == y
            case "gt": 
                return x > y
            case "lt": 
                return x < y
            case "ge": 
                return x >= y
            case "le": 
                return x <= y
            case _:
                return False #ERROR

    @abstractmethod
    def chek_compilance(self, fpath: str) -> bool:
        pass

    @abstractmethod
    def chek_arhive_compilance(self, z_info: ZipInfo) -> bool:
        pass