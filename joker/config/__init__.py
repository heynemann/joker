#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com


from derpconf.config import Config  # NOQA

Config.define(
    'ROUTES',
    [],
    'List of routes using middlewares to include in this server',
    'Routing'
)
