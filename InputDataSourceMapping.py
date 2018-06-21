import json
import re

from Utilities import load_dirty_json


class InputDataSourceMapping:
    input_data_source = None
    path = ''

    def __init__(self, input_data_source, path):
        self.input_data_source = input_data_source
        self.path = path

    def get_value(self):
        data_type = self.input_data_source.data_type
        if data_type == 'json':
            last_snapshot = self.input_data_source.last_data_snapshot
            if last_snapshot == '':
                return 0
            fixed_last_snapshot = re.sub('([{,:])(\w+)([},:])', '\\1\"\\2\"\\3', str(last_snapshot, 'utf-8'))
            # fixed_last_snapshot = re.sub('([{,:])(\w+)([},:])','\\1\"\\2\"\\3',str(last_snapshot))
            # fixed_last_snapshot = last_snapshot
            last_snapshot_json_document = json.loads(fixed_last_snapshot)
            # fixed_last_snapshot = load_dirty_json(last_snapshot)
            # return fixed_last_snapshot
            return last_snapshot_json_document[self.path]
        elif data_type == 'raw':
            return self.input_data_source.last_data_snapshot
        else:
            print('unknown data type ' + data_type)