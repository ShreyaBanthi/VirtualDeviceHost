import logging
import paho.mqtt.client as mqtt


class BrokerConnection:
    client = None
    handler_method = None
    connection_name = ''
    qos_level = 0

    def __init__(self, connection_name, hostname, qos_level=0):
        self.connection_name = connection_name
        self.qos_level = qos_level

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(hostname, 1883, 60)

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        logging.info("BrokerConnection connected ")

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("#", qos=self.qos_level)

    def on_message(self, client, userdata, msg):
        self.handler_method(self, msg.topic, msg)

    def start_receiving(self, handler_method):
        self.handler_method = handler_method
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        # self.client.loop_forever()
        self.client.loop_start()

    def stop_receiving(self):
        self.client.loop_stop(False)

    def publish(self, topic, payload, qos_level):
        self.client.publish(topic, payload, qos=qos_level)
