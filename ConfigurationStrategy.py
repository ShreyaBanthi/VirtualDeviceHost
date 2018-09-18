from abc import ABCMeta, abstractmethod


class ConfigurationStrategy(metaclass=ABCMeta):

    @abstractmethod
    def create_broker_connections(self):
        return []

    @abstractmethod
    def create_virtual_devices(self):
        return []

    @abstractmethod
    def is_monitoring_enabled(self):
        return False

    @abstractmethod
    def get_monitoring_output_topic(self):
        return ''

    @abstractmethod
    def get_monitoring_broker_connection(self):
        return ''

    @abstractmethod
    def get_monitoring_grace_period_duration(self):
        return ''
