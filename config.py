import argparse
import sys
from log import build_logger, logging
from utilities import unix_time_now


def build_arg_parser():
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument('--log-level', help='Set the logging level')
    parser.add_argument('--net', help='Set net to operate on',
                        choices=['test', 'stage', 'main'], required=True)
    return parser.parse_args()


def init():
    global start_time
    global logger
    global args

    start_time = unix_time_now()
    args = build_arg_parser()

    if args.log_level:
        global log_level
        log_level = getattr(logging, args.log_level.upper())
    logger = build_logger()


# define global variables
start_time = None
logger = None
log_level = logging.INFO
args = None
