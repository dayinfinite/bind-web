#!/usr/bin/env python
# coding=utf-8

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
import config

print config.user
