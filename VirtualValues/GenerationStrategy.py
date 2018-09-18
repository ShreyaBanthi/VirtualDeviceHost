from abc import ABCMeta, abstractmethod


class GenerationStrategy(metaclass=ABCMeta):
    virtual_value_group = None
    wait_event = None

    def __init__(self):
        pass

    def set_virtual_value_group(self, virtual_value_group):
        self.virtual_value_group = virtual_value_group
        self.wait_event = self.virtual_value_group.wait_event

    def start(self):
        pass

    @abstractmethod
    def should_generate(self):
        return False
