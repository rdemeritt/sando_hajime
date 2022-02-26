import logging
import sys
from utilities import unix_time_now
import config


def build_logger():
    logger_name = sys.argv[0]
    formatter = logging.Formatter("[%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:%(filename)s(%(lineno)s)] "
                                  "%(message)s", "%Y-%m-%dT%H:%M:%S")
    _logger = logging.getLogger(logger_name)

    # log to file
    fh = logging.FileHandler('%s_%s.log' % (logger_name, unix_time_now()))
    fh.setLevel(config.log_level)
    fh.setFormatter(formatter)

    # log to the console as well
    ch = logging.StreamHandler()
    ch.setLevel(config.log_level)
    ch.setFormatter(formatter)

    logging.basicConfig(level=config.log_level, handlers=(fh, ch))
    return _logger
