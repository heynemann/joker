#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from preggy import expect
from ujson import dumps

from tests.base import ApiTestCase


class ApiServerTestCase(ApiTestCase):
    def test_can_create_schema(self):
        response = self.fetch('/schema', method="PUT", body=dumps({
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"},
            }
        }))
        expect(response.code).to_equal(200)
        expect(response.body).to_be_like('OK')

    def test_cant_create_invalid_schema(self):
        response = self.fetch('/schema', method="PUT", body=dumps({
            "properties": {
                "name": {"type": "invalid-type"},
                "email": {"type": "string"},
            }
        }))
        expect(response.code).to_equal(400)
        expect(response.body).to_equal('could not create specified schema')
