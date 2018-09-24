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
        vd = VirtualDevice('Room 1')

        vf = VirtualFunction('Light-Switcher', 'main', 'maproject/light/1')
        vf.add_output_target(OutputTarget('Light 2', 'main', 'jarvis/lightstrip/103/pushes',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:103')))
        vf.add_output_target(OutputTarget('Light 3', 'main', 'jarvis/lightstrip/105/pushes',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:105')))
        vf.add_output_target(OutputTarget('Light 4', 'main', 'jarvis/lightstrip/107/pushes',
                                          RegexReplaceOutputGeneratorStrategy('myId:(\d)*', 'myId:107')))

        vd.add_virtual_function(vf)

        vds.append(vd)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("main", "192.168.1.100")
        broker_connections.append(input_connection)

        return broker_connections

    def is_monitoring_enabled(self):
        return False

    def get_monitoring_grace_period_duration(self):
        return None

    def get_monitoring_broker_connection(self):
        return None

    def get_monitoring_output_topic(self):
        return None
