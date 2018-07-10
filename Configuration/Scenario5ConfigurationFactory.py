from ConfigurationFactory import ConfigurationFactory
from VirtualDevice import VirtualDevice
from VirtualFunctions.VirtualFunction import VirtualFunction
from VirtualFunctions.OutputTarget import OutputTarget
from BrokerConnection import BrokerConnection
from VirtualFunctions.OutputGeneratorStrategies.CopyOutputGeneratorStrategy import CopyOutputGeneratorStrategy


class Scenario5ConfigurationFactory(ConfigurationFactory):
    def get_device_health_broker_connection(self):
        return 'output'

    def get_device_health_topic(self):
        return 'maproject/health/device-states'

    def create_virtual_devices(self):
        vds = []
        vd = VirtualDevice('Room 12')

        vf = VirtualFunction('Light-Switcher', 'input', 'maproject/light/1')
        vf.add_output_target(OutputTarget('Light 2', 'output', 'maproject/light/2', CopyOutputGeneratorStrategy()))
        vf.add_output_target(OutputTarget('Light 3', 'output', 'maproject/light/3', CopyOutputGeneratorStrategy()))
        vf.add_output_target(OutputTarget('Light 4', 'output', 'maproject/light/4', CopyOutputGeneratorStrategy()))
        vf.add_output_target(OutputTarget('Light 5', 'output', 'maproject/light/5', CopyOutputGeneratorStrategy()))

        vd.add_virtual_function(vf)

        vds.append(vd)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.1.100")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "192.168.1.100")
        broker_connections.append(output_connection)

        return broker_connections

    def is_device_health_monitoring_enabled(self):
        return True
