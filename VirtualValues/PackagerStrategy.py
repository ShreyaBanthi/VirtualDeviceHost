from abc import ABCMeta, abstractmethod


class PackagerStrategy(metaclass=ABCMeta):

    @abstractmethod
    def package(self, virtual_values, synthesized_values):
        return None
