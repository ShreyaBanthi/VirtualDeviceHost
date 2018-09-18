from abc import ABCMeta, abstractmethod


class ParsingStrategy(metaclass=ABCMeta):

    @abstractmethod
    def parse(self, raw_payload):
        return None
