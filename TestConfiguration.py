from VirtualValue import VirtualValue
from InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValueGroup import VirtualValueGroup


class TestConfiguration:
    @staticmethod
    def create_test_virtual_device(broker_connection):
        vd = VirtualDevice('TestDevice')

        # generate input data sources
        ids1 = InputDataSource('Sensor1', "maproject/environment/2/updates", "json", 5)
        vd.add_input_data_source(ids1)
        ids2 = InputDataSource('Sensor2', "maproject/temperature/2/updates", "raw", 5)
        vd.add_input_data_source(ids2)

        vvg1 = VirtualValueGroup('facility-system/temperature/room-1', 2,
                                 '{measured_temperature:$0, max_temperature:$1}', broker_connection)

        # add virtual values
        vv1 = VirtualValue('Temp', '$0', 'math-average', 'simple-float')
        vv1.add_mapping(ids1, 'temperature')
        vv1.add_mapping(ids2, '')
        vvg1.add_virtual_value(vv1)

        vv2 = VirtualValue('Temp', '$1', 'math-max', 'simple-float')
        vv2.add_mapping(ids1, 'temperature')
        vv2.add_mapping(ids2, '')
        vvg1.add_virtual_value(vv2)

        vd.add_virtual_value_group(vvg1)

        return vd
