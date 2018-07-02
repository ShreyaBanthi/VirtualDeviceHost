from AggregatorStrategy import AggregatorStrategy


class MostCurrentSnapshotAggregatorStrategy(AggregatorStrategy):

    def __init__(self):
        pass

    def aggregate(self, mappings):
        most_current_mapping = None
        most_current_snapshot_date = None
        for m in mappings:
            snapshot_date = m.input_data_source.last_data_snapshot_timestamp
            if most_current_snapshot_date is None or snapshot_date > most_current_snapshot_date:
                most_current_mapping = m
                most_current_snapshot_date = snapshot_date
        most_current_value = most_current_mapping.get_value()
        return [most_current_value]
