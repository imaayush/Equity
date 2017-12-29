import unittest
import os
from unittest import TestCase
from bhavcopy_script import scrape_dowload_store_bhavcopy
from services.redis_services import RedisServices
import cherrypy

from cherrypy.test import helper
from routes import Routes


class BhavcopyScriptTest(TestCase):
    def test_bahvcopy_script(self):
        scrape_dowload_store_bhavcopy()
        rdb = RedisServices()
        comp = rdb.get_top_ten()
        self.assertEqual(len(comp), 10)


class CherrypyTest(helper.CPWebCase):
    def setup_server():
        cherrypy.tree.mount(Routes())

    setup_server = staticmethod(setup_server)

    def test_get_top_ten_companies(self):
        self.getPage("/companies")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')

    def test_get_by_name(self):
        self.getPage("/companies?company_name=HDFC")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
