from AggregatorStrategy import AggregatorStrategy


from Utilities import every, is_number


class SimpleFloatSnapshotAggregatorStrategy(AggregatorStrategy):

    def __init__(self):
        pass

    def aggregate(self, mappings):
        values = []
        for m in mappings:
            raw_val = m.get_value()
            if is_number(raw_val):
                val = float(m.get_value())
                values.append(val)
        return values
