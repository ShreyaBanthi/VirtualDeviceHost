from abc import ABCMeta, abstractmethod


class OutputGeneratorStrategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def generate(self, source_message):
        return None
