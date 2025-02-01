from factory.abs_fruit_factory import AbstractFruitFactory
from fruit.null_fruit import NullFruit


class NullFactory(AbstractFruitFactory):
    def prepare_breakfast(self):
        fruit = NullFruit()
        return fruit
