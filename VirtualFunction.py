class OutputTarget:
    def __init__(self):
        pass


# output
class VirtualFunction:
    name = 'unnamed'
    trigger_topic = ''

    def __init__(self, name, trigger_topic):
        self.name = name
        self.trigger_topic = trigger_topic

    def execute(self):
        pass