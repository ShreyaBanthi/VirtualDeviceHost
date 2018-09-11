from datetime import timedelta
from ConfigurationStrategy import ConfigurationStrategy
from BrokerConnection import BrokerConnection


class Scenario4ConfigurationFactory(ConfigurationStrategy):
    def get_monitoring_broker_connection(self):
        return 'output'

    def get_monitoring_output_topic(self):
        return 'maproject/health/device-states'

    def create_virtual_devices(self):
        vds = []

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.1.100")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "192.168.1.100")
        broker_connections.append(output_connection)

        return broker_connections

    def is_monitoring_enabled(self):
        return True

    def get_monitoring_grace_period_duration(self):
        return timedelta(seconds=5)
