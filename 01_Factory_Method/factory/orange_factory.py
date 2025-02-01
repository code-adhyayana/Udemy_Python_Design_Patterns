from factory.abs_fruit_factory import AbstractFruitFactory
from fruit.orange import Orange


class OrangeFactory(AbstractFruitFactory):
    def prepare_breakfast(self):
        fruit = Orange()
        return fruit
