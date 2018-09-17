from abc import ABCMeta, abstractmethod


class OutputGeneratorStrategy(metaclass=ABCMeta):

    @abstractmethod
    def generate(self, source_message):
        return None
