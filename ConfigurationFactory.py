import importlib


class ConfigurationFactory:
    def create_configuration(self, configuration_name):
        mod = importlib.import_module('Configuration.' + configuration_name)
        conf_class = getattr(mod, configuration_name)
        conf_instance = conf_class()
        return conf_instance
