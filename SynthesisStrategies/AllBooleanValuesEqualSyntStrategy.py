from SyntStrategy import SyntStrategy


class AllBooleanValuesEqualSyntStrategy(SyntStrategy):

    expected_value = False
    default_value = False

    def __init__(self, expected_value, default_value):
        self.expected_value = expected_value
        self.default_value = default_value

    def parse_truthiness(self, value):
        if value:
            return True
        elif isinstance(value, str) & (value.lower() == 'true'):
            return True
        elif value == 1:
            return True
        elif isinstance(value, str) & (value.lower() == 'false'):
            return False
        elif value == 0:
            return False

    def synthesize(self, values):
        if len(values) == 0:
            return self.default_value

        for v in values:
            truthiness = self.parse_truthiness(v)
            if truthiness != self.expected_value:
                return False;

        return True
