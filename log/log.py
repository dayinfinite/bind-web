# -*- coding:utf-8 -*-
# __author__ = 'dayinfinte'

import logging
import sys
from logging.config import fileConfig

def Log():
    fileConfig('../config/logging_config.ini')
    logger = logging.getLogger()