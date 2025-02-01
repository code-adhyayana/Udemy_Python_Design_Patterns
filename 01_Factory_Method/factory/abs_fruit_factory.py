from abc import ABC, abstractmethod


class AbstractFruitFactory(ABC):
    @abstractmethod
    def prepare_breakfast(self):
        pass
