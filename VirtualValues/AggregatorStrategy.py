from abc import ABCMeta, abstractmethod


class AggregatorStrategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def aggregate(self, input_data_sources):
        pass

    @abstractmethod
    def synthesize_value(self):
        return None
