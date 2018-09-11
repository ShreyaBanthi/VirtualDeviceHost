import json
import re
import logging

from Utilities import load_dirty_json


class InputDataSourceMapping:
    input_data_source = None
    path = ''

    def __init__(self, input_data_source, path):
        self.input_data_source = input_data_source
        self.path = path

    def get_inner_json_value(self, json_element, path):
        # json_element_string = json_element.dumps()

        first_dot_index = path.find('.')
        first_brace_index = path.find('{')

        if first_dot_index == -1 and first_brace_index == -1:
            return json_element[path]
        if first_dot_index < first_brace_index:  # if object
            object_name = path[0, first_dot_index]
            return self.get_inner_json_value(json_element[object_name], path[first_dot_index:])
        if first_brace_index < first_dot_index:  # array
            array_name = path[0, first_brace_index]
            return self.get_inner_json_value(json_element[array_name], path[first_brace_index:])
        else:
            return None

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
            # return last_snapshot_json_document[self.path]
            # return self.get_inner_json_value(last_snapshot_json_document, self.path)
            return self.get_inner_json_value(last_snapshot_json_document, self.path)
        elif data_type == 'raw':
            return self.input_data_source.last_data_snapshot
        else:
            logging.warning('unknown data type ' + data_type)