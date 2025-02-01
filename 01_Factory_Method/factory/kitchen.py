from importlib import import_module
from inspect import getmembers, isclass, isabstract
from factory.abs_fruit_factory import AbstractFruitFactory


def factory_loader(factory_name):

    try:
        factory_module = import_module("." + factory_name, "factory")
    except ImportError:
        factory_module = import_module(".null_factory", "factory")

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for _, class_name in classes:
        if issubclass(class_name, AbstractFruitFactory):
            return class_name()

