

'''
class AverageBooleanSyntStrategy(SyntStrategy):

    def __init__(self):
        pass

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
        true_count = 0
        false_count = 0

        for v in values:
            truthiness = self.parse_truthiness(v)
            if truthiness:
                true_count += 1
            else:
                false_count += 1

        if true_count > false_count:
            return True
        else:
            return False
'''