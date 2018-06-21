from functools import reduce

from SyntStrategy import SyntStrategy


class MovingAverageSyntStrategy(SyntStrategy):
    data_set = []
    data_set_size = 5

    def __init__(self, data_set_size):
        self.data_set_size = data_set_size

    def synthesize(self, values):
        float_values = [float(i) for i in values]
        avg = round(sum(float_values) / len(float_values), 2)
        self.data_set.append(avg)
        if len(self.data_set) > self.data_set_size:
            self.data_set.pop(0)
        moving_avg = reduce(lambda x, y: x + y, self.data_set) / len(self.data_set)
        return moving_avg
