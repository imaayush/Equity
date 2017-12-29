import os
from unittest import TestCase
from services.redis_services import RedisServices
from services.equity_parser import EquityParser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class RedisServicesTest(TestCase):
    def test_redis_services(self):
        parser = EquityParser()
        companies_details = parser.parse(ROOT_DIR + "/data/EQ261217.CSV")
        self.assertEqual(len(companies_details), 13)
        self.assertEqual(companies_details[0].get("SC_CODE"), "500002")
        rdb = RedisServices()
        rdb.post(companies_details)
        comp = rdb.get_top_ten()
        # test get top ten
        self.assertEqual(comp[0], companies_details[0])
        # test get by name
        comp = rdb.get_by_name(companies_details[0].get("SC_NAME"))
        self.assertEqual(comp, companies_details[0])
