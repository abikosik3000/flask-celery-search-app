from abc import ABC , abstractmethod
from zipfile import ZipInfo

from pydantic import validator
from redis_om import EmbeddedJsonModel, Field


class Filter(EmbeddedJsonModel,ABC):
    '''an abstract filter for search file that uses comparisons'''
    operator: str
    
    @validator('operator')
    def check_allowed_operator(cls,v):
        if(v not in ('eq', 'gt', 'lt', 'ge', 'le')):
            raise ValueError('operator must be in eq, gt, lt, ge, le')
        return v

    def _comparate(self, x) -> bool:
        '''apply a filter and returns the result of the comparison'''
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
            
    @abstractmethod
    def get_value(self):
        '''return filter value to comparation'''
        pass

    @abstractmethod
    def chek_compilance(self, fpath: str) -> bool:
        '''checks if the file passes the filter'''
        pass

    @abstractmethod
    def chek_arhive_compilance(self, z_info: ZipInfo) -> bool:
        '''checks if the arhive file passes the filter'''
        pass