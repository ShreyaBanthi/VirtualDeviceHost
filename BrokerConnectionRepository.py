class BrokerConnectionRepository:
    _broker_connections = []

    def __init__(self):
        pass

    def get_all_broker_connections(self):
        return self._broker_connections

    def get_broker_connection(self, connection_name):
        for bc in self._broker_connections:
            if bc.connection_name == connection_name:
                return bc
        return None

    def add_broker_connection(self, new_broker_connection):
        self._broker_connections.append(new_broker_connection)
