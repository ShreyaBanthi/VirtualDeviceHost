from abc import ABCMeta, abstractmethod


class SyntStrategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def synthesize(self, values):
        pass
