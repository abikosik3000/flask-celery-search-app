from abc import ABC , abstractmethod
from zipfile import ZipInfo

from pydantic import validator
from redis_om import EmbeddedJsonModel, Field


class Filter(EmbeddedJsonModel,ABC):
    operator: str
    
    @validator('operator')
    def check_allowed_operator(cls,v):
        if(v not in ('eq', 'gt', 'lt', 'ge', 'le')):
            raise ValueError('operator must be in eq, gt, lt, ge, le')
        return v

    def _comparate(self, x) -> bool:
        y = self.get_value()
        #print(x,y , x - y)
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
    def get_value(self):
        pass

    @abstractmethod
    def chek_compilance(self, fpath: str) -> bool:
        pass

    @abstractmethod
    def chek_arhive_compilance(self, z_info: ZipInfo) -> bool:
        pass