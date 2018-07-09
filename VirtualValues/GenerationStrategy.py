from abc import ABCMeta, abstractmethod


class GenerationStrategy(metaclass=ABCMeta):

    def __init__(self, virtual_value_group):
        pass

    @abstractmethod
    def start(self):
        return None

    @abstractmethod
    def stop(self):
        return None

    @abstractmethod
    def package(self):
        return None
