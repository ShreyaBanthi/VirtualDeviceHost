import time
import traceback
import json
import re


def delayed_every(first_delay, delay, task):
    time.sleep(first_delay)
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            task()
        except Exception:
            traceback.print_exc()
        # skip tasks if we are behind schedule:
        next_time += (time.time() - next_time) // delay * delay + delay

def every(delay, task):
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            task()
        except Exception:
            traceback.print_exc()
        # skip tasks if we are behind schedule:
        next_time += (time.time() - next_time) // delay * delay + delay


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def load_dirty_json(dirty_json):
    regex_replace = [(r"([ \{,:\[])(u)?'([^']+)'", r'\1"\3"'), (r" False([, \}\]])", r' false\1'), (r" True([, \}\]])",
                                                                                                    r' true\1')]
    for r, s in regex_replace:
        dirty_json = re.sub(r, s, dirty_json)
    clean_json = json.loads(dirty_json)
    return clean_json


def get_inner_json_value(json_element, path):
    if path == '':
        return json_element

    first_dot_index = path.find('.')
    first_brace_index = path.find('[')

    if first_dot_index == -1 and first_brace_index == -1:
        return json_element[path]
    if first_dot_index < first_brace_index:  # if object
        object_name = path[0:first_dot_index]
        return get_inner_json_value(json_element[object_name], path[first_dot_index:])
    if first_brace_index < first_dot_index:  # array
        array_name = path[0:first_brace_index]
        closing_brace_index = path.find(']')
        array_target_index = int(path[first_brace_index+1:closing_brace_index])
        remaining_path = path[closing_brace_index+1:]
        if len(remaining_path) > 1 and remaining_path[0] == '.':
            remaining_path = remaining_path[1:]
        return get_inner_json_value(json_element[array_name][array_target_index], remaining_path)
    else:
        return None


def get_json_value(data, path):
    last_snapshot = data
    if last_snapshot == '':
        return 0
    fixed_last_snapshot = last_snapshot
    # fixed_last_snapshot = re.sub('([{,:])(\w+)([},:])', '\\1\"\\2\"\\3', str(last_snapshot, 'utf-8'))
    # fixed_last_snapshot = fixed_last_snapshot.replace("\'", '"')
    # fixed_last_snapshot = fixed_last_snapshot.replace(":nan", ':null')
    ### fixed_last_snapshot = re.sub('([{,:])(\w+)([},:])','\\1\"\\2\"\\3',str(last_snapshot))
    # fixed_last_snapshot = last_snapshot
    last_snapshot_json_document = json.loads(fixed_last_snapshot)
    # fixed_last_snapshot = load_dirty_json(last_snapshot)
    # return fixed_last_snapshot
    # return last_snapshot_json_document[self.path]
    # return self.get_inner_json_value(last_snapshot_json_document, self.path)
    return get_inner_json_value(last_snapshot_json_document, path)
