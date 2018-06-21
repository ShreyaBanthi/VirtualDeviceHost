from abc import ABCMeta, abstractmethod


class ConfigurationFactory(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def create_broker_connections(self):
        return []

    @abstractmethod
    def create_virtual_devices(self):
        return []

    @abstractmethod
    def is_device_health_monitoring_enabled(self):
        return False

    @abstractmethod
    def get_device_health_topic(self):
        return ''

    @abstractmethod
    def get_device_health_broker_connection(self):
        return ''
