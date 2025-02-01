from factory.abs_fruit_factory import AbstractFruitFactory
from fruit.apple import Apple


class AppleFactory(AbstractFruitFactory):
    def prepare_breakfast(self):
        fruit = Apple()
        return fruit
