from abc import ABCMeta, abstractmethod


class AggregatorStrategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def aggregate(self):
        return []
