from abc import ABC, abstractmethod


class AbstractFruit(ABC):
    @abstractmethod
    def eat(self):
        pass