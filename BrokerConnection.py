import paho.mqtt.client as mqtt


class BrokerConnection:
    client = None
    handler_method = None

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("#")

    def on_message(self, client, userdata, msg):
        self.handler_method(msg.topic, msg)

    def __init__(self, hostname, handler_method):
        self.handler_method = handler_method

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(hostname, 1883, 60)

    def start_receiving(self):
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        # self.client.loop_forever()
        self.client.loop_start()

    def stop_receiving(self):
        self.client.loop_stop(False)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)
