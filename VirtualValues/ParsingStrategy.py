from abc import ABCMeta, abstractmethod


class ParsingStrategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def parse(self, raw_payload):
        return None
