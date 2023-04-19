from redis_om import EmbeddedJsonModel, Field
from abc import ABC , abstractmethod

class Filter(EmbeddedJsonModel,ABC):
    value: str = Field(index=True)
    operator: str = Field(index=True)

    @abstractmethod
    def chek_compilance(self, fpath: str) -> bool:
        pass