#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from preggy import expect
import tornado.gen

from joker import __version__
from joker.middleware import Middleware
from joker.config import Config
from joker.server import JokerServer
from tests.base import ApiTestCase


class JokerServerTestCase(ApiTestCase):
    def test_healthcheck(self):
        response = self.fetch('/healthcheck')
        expect(response.code).to_equal(200)
        expect(response.body).to_be_like('WORKING')

    def test_server_version(self):
        response = self.fetch('/version')
        expect(response.code).to_equal(200)
        expect(response.body).to_be_like(__version__)


class TestMiddleware(Middleware):
    @tornado.gen.coroutine
    def process(self, app, handler, request, response):
        response.body.append('test')
        response.set_header('X-Server-Name', 'test-server.api.com')


class BasicMiddlewareTestCase(ApiTestCase):
    def get_server(self):
        class TestServer(JokerServer):
            def get_routes(self):
                return (
                    ('/test', [TestMiddleware]),
                )

        cfg = Config(**self.get_config())
        self.server = TestServer(
            config=cfg
        )
        return self.server

    def test_use_middleware(self):
        response = self.fetch('/test')
        expect(response.code).to_equal(200)
        expect(response.body).to_be_like('test')

    def test_can_get_headers_with_middleware(self):
        response = self.fetch('/test')
        expect(response.headers).to_include('X-Server-Name')
        expect(response.headers['X-Server-Name']).to_equal('test-server.api.com')
