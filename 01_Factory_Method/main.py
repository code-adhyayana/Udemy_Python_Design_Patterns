# Apple
# Mango
# client
from factory.kitchen import factory_loader

for fruit_name in ['apple_factory', 'mango_factory', 'orange_factory', 'NA']:
    fruit_factory = factory_loader(fruit_name)
    fruit = fruit_factory.prepare_breakfast()
    fruit.eat()
