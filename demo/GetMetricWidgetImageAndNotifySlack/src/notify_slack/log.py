# -*- coding: utf-8 -*-

import logging

def get_logger(log_level):
    print('log_level: ' + log_level.upper())
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    numeric_level = getattr(logging, log_level.upper(), None)
    handler.setLevel(numeric_level)
    logger.setLevel(numeric_level)
    logger.handlers = [handler]
    logger.propagate = False
    return logger
