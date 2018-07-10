from ConfigurationFactory import ConfigurationFactory
from VirtualValue import VirtualValue
from InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValueGroup import VirtualValueGroup
from BrokerConnection import BrokerConnection
from SynthesisStrategies.MaximumSyntStrategy import MaximumSyntStrategy
from SynthesisStrategies.MovingAverageSyntStrategy import MovingAverageSyntStrategy
from SynthesisStrategies.AverageBooleanSyntStrategy import AverageBooleanSyntStrategy
from SynthesisStrategies.AllBooleanValuesEqualSyntStrategy import AllBooleanValuesEqualSyntStrategy
from AggregatorStrategies.DoorSensorIsClosedAggregatorStrategy import DoorSensorIsClosedAggregatorStrategy


class Scenario2ConfigurationFactory(ConfigurationFactory):
    def get_device_health_broker_connection(self):
        return 'main'

    def get_device_health_topic(self):
        return 'maproject/health/device-states'

    def create_virtual_devices(self):
        vds = []

        vd = VirtualDevice('Building 1')

        # generate input data sources
        ids1 = InputDataSource('DoorSensor1', 'main', "maproject/environment/2/updates", "json", 1)
        vd.add_input_data_source(ids1)
        ids2 = InputDataSource('DoorSensor2', 'main', "maproject/temperature/2/updates", "json", 1)
        vd.add_input_data_source(ids2)
        ids3 = InputDataSource('WindowSensor1', 'main', "maproject/temperature/2/updates", "json", 1)
        vd.add_input_data_source(ids3)

        vvg1 = VirtualValueGroup('facility-system/buildings/building/1', 5,
                                 '{all_doors_closed:$0, all_windows_closed:$1}',
                                 "main")

        # add virtual values
        vv1 = VirtualValue('All Doors Closed', '$0')
        vv1.add_mapping(ids1, 'newState')
        vv1.add_mapping(ids2, 'newState')
        vv1.add_mapping(ids3, 'newState')
        vv1.set_aggregator_strategy(DoorSensorIsClosedAggregatorStrategy())
        vv1.set_synthesis_strategy(AllBooleanValuesEqualSyntStrategy(True, False))
        vvg1.add_virtual_value(vv1)

        vv2 = VirtualValue('All Windows Closed', '$1')
        vv2.add_mapping(ids1, 'newState')
        vv2.add_mapping(ids2, 'newState')
        vv2.add_mapping(ids3, 'newState')
        vv2.set_aggregator_strategy(DoorSensorIsClosedAggregatorStrategy())
        vv2.set_synthesis_strategy(AllBooleanValuesEqualSyntStrategy(True, False))
        vvg1.add_virtual_value(vv2)

        vd.add_virtual_value_group(vvg1)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("main", "192.168.1.3")
        broker_connections.append(input_connection)

        return broker_connections

    def is_device_health_monitoring_enabled(self):
        return True
