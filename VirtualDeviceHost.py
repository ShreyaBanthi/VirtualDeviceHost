import logging

from VirtualDeviceRepository import VirtualDeviceRepository
from Monitoring.DeviceHealthPublisher import DeviceHealthPublisher
from ConfigurationFactory import ConfigurationFactory
from BrokerConnectionRepository import BrokerConnectionRepository


class VirtualDeviceHost:
    virtual_device_repository = None
    broker_connection_repository = None
    device_health_publisher = None
    active_configuration = None

    def initialize(self, configuration_name):
        configuration_factory = ConfigurationFactory()
        self.active_configuration = configuration_factory.create_configuration(configuration_name)

        self.virtual_device_repository = VirtualDeviceRepository()
        self.broker_connection_repository = BrokerConnectionRepository()

        broker_connections = self.active_configuration.create_broker_connections()
        for bc in broker_connections:
            self.broker_connection_repository.add_broker_connection(bc)

        virtual_devices = self.active_configuration.create_virtual_devices()
        for vd in virtual_devices:
            self.virtual_device_repository.add_virtual_device(vd)

        if self.active_configuration.is_monitoring_enabled():
            device_health_publisher_broker_connection = self.broker_connection_repository.get_broker_connection(
                self.active_configuration.get_monitoring_broker_connection())
            self.device_health_publisher = DeviceHealthPublisher(self.virtual_device_repository,
                                                                 device_health_publisher_broker_connection,
                                                                 self.active_configuration.get_monitoring_output_topic(), 5,
                                                                 self.active_configuration.get_monitoring_grace_period_duration())

    def start(self):
        # self.broker_connection.start_receiving(self.on_handle_message)
        for bc in self.broker_connection_repository.get_all_broker_connections():
            bc.start_receiving(self.on_handle_message)

        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        for vd in virtual_devices:
            vd.start(self.broker_connection_repository)

        if self.active_configuration.is_monitoring_enabled():
            self.device_health_publisher.start()

    def stop(self):
        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        for vd in virtual_devices:
            vd.stop()

        if self.active_configuration.is_monitoring_enabled():
            self.device_health_publisher.stop()

        for bc in self.broker_connection_repository.get_all_broker_connections():
            bc.stop_receiving()

    def on_handle_message(self, broker_connection, topic, msg):
        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        for vd in virtual_devices:
            vd.handle_mqtt_message(broker_connection, topic, msg)
