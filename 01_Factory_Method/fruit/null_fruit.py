from fruit.abs_fruit import AbstractFruit


class NullFruit(AbstractFruit):
    def eat(self):
        print("Unknown Fruit")

