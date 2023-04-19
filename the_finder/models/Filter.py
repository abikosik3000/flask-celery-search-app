from redis_om import EmbeddedJsonModel, Field
from abc import ABC , abstractmethod

class Filter(EmbeddedJsonModel,ABC):
    value: str = Field(index=True)
    operator: str = Field(index=True)

    def get_value(self):
        return self.value

    def _comparate(self, x) -> bool:

        y = self.get_value()
        print(x , self.operator , y  )
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