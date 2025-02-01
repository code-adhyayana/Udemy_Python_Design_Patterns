from factory.abs_fruit_factory import AbstractFruitFactory
from fruit.mango import Mango


class MangoFactory(AbstractFruitFactory):
    def prepare_breakfast(self):
        fruit = Mango()
        return fruit
