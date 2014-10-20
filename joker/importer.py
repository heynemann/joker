#!/usr/bin/python
# -*- coding: utf-8 -*-

# this file is part of joker.
# https://github.com/heynemann/joker

# licensed under the mit license:
# http://www.opensource.org/licenses/mit-license
# copyright (c) 2014 bernardo heynemann heynemann@gmail.com


def get_class(full_name):
    module_name, class_name = full_name.rsplit('.', 1)

    module = __import__(module_name)

    if '.' in module_name:
        module = reduce(getattr, module_name.split('.')[1:], module)

    return getattr(module, class_name)
