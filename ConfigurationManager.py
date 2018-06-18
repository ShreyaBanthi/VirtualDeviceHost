from ConfigurationFactory import ConfigurationFactory

import importlib


class ConfigurationManager:
    def __init__(self):
        pass

    def find_configuration(self, configuration_name):
        mod = importlib.import_module('Configuration.' + configuration_name)
        conf_class = getattr(mod, configuration_name)
        conf_instance = conf_class()
        #configurations = ConfigurationFactory.__subclasses__()
        # if len(configurations) == 0:
        #     raise Exception('no configurations found!')
        # elif len(configurations) > 1:
        #     raise Exception('multiple configurations found!')
        # else:
        #     return configurations[0]
