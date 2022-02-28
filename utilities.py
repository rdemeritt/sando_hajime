"""
common functions and utilities that i use...
"""

from time import time
import json
import config


def set_net(_net=None):
    if not _net:
        net = config.args.net
    else:
        net = _net
    return net


def unix_time_now():
    return int(time())


def get_json_file_contents(_file):
    with open(_file) as file:
        return json.load(file)


def write_json(_json, _file):
    with open(_file, 'w+') as file:
        json.dump(_json, file, indent=4, default=_jsonize_it)
        # json.dump(_json, file)
    return True


def _jsonize_it(_object):
    if isinstance(_object, set):
        return list(_object)
    try:
        return _object.__dict__
    except AttributeError:
        return str(_object)


def append_json(_dict, _json):
    _json.append(_dict)
    return True


def whoami():
    from sys import _getframe
    return _getframe(1).f_code.co_name
