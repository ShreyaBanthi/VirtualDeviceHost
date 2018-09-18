import threading
import logging
from Monitoring.MonitoringOutputMessage import MonitoringOutputMessage
from Utilities import delayed_every


class DeviceHealthPublisher:
    virtual_device_repository = None
    broker_connection = None
    publish_topic = ''
    publish_cycle_in_s = 60
    thread = None
    grace_period_duration = None

    def __init__(self, virtual_device_repository, broker_connection, publish_topic, publish_cycle_in_s,
                 grace_period_duration):
        self.virtual_device_repository = virtual_device_repository
        self.broker_connection = broker_connection
        self.publish_topic = publish_topic
        self.publish_cycle_in_s = publish_cycle_in_s
        self.grace_period_duration = grace_period_duration
        grace_period_in_seconds = 0
        if grace_period_duration is not None:
            grace_period_in_seconds = grace_period_duration.total_seconds()
        self.thread = threading.Thread(target=lambda: delayed_every(grace_period_in_seconds, publish_cycle_in_s,
                                                                    self.publish_health_state))
        self.thread.setDaemon(True)

    def start(self):
        self.thread.start()

    def stop(self):
        # nothing to do as daemon thread would be stopped automatically when process ends
        pass

    def publish_health_state(self):
        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        output = MonitoringOutputMessage()

        # check all devices
        for vd in virtual_devices:
            if vd.check_if_healthy():
                output.states[vd.name] = "normal"
            else:
                output.states[vd.name] = "degraded"

        # convert to json
        output_json = output.to_json()

        logging.info('Publishing health state: ' + output_json)
        self.broker_connection.publish(self.publish_topic, output_json, qos_level=0)
