from abc import ABCMeta, abstractmethod


class PackagerStrategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def package(self, virtual_values, synthesized_values):
        return None
