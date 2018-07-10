from ConfigurationFactory import ConfigurationFactory
from VirtualValue import VirtualValue
from InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValueGroup import VirtualValueGroup
from BrokerConnection import BrokerConnection
from SynthesisStrategies.MaximumSyntStrategy import MaximumSyntStrategy
from SynthesisStrategies.MovingAverageSyntStrategy import MovingAverageSyntStrategy


class Scenario3ConfigurationFactory(ConfigurationFactory):
    def get_device_health_broker_connection(self):
        return 'output'

    def get_device_health_topic(self):
        return 'maproject/health/device-states'

    def create_virtual_devices(self):
        vds = []

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.1.3")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "192.168.1.3")
        broker_connections.append(output_connection)

        return broker_connections

    def is_device_health_monitoring_enabled(self):
        return True
