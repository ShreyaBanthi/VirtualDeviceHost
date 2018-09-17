from ConfigurationStrategy import ConfigurationStrategy
from VirtualDevice import VirtualDevice
from VirtualFunctions.VirtualFunction import VirtualFunction
from VirtualFunctions.OutputTarget import OutputTarget
from BrokerConnection import BrokerConnection
from VirtualFunctions.OutputGeneratorStrategies.RegexReplaceOutputGeneratorStrategy \
    import RegexReplaceOutputGeneratorStrategy


class Scenario6ConfigurationStrategy(ConfigurationStrategy):
    def create_virtual_devices(self):
        vds = []
        vd = VirtualDevice('Room 12')

        vf = VirtualFunction('Light-Switcher', 'input', 'maproject/light/1')
        vf.add_output_target(OutputTarget('Light 2', 'output', 'maproject/light/2',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:101')))
        vf.add_output_target(OutputTarget('Light 3', 'output', 'maproject/light/3',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:102')))
        vf.add_output_target(OutputTarget('Light 4', 'output', 'maproject/light/4',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:103')))
        vf.add_output_target(OutputTarget('Light 5', 'output', 'maproject/light/5',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:104')))

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

    def is_monitoring_enabled(self):
        return False

    def get_monitoring_grace_period_duration(self):
        return None

    def get_monitoring_broker_connection(self):
        return None

    def get_monitoring_output_topic(self):
        return None
