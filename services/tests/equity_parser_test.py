import os
from unittest import TestCase
from services.equity_parser import EquityParser
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class EquityParserTest(TestCase):
    def test_parser_equity_pass(self):
        parser = EquityParser()
        companies_details = parser.parse(ROOT_DIR + "/data/EQ261217.CSV")
        self.assertEqual(len(companies_details), 13)
        self.assertEqual(companies_details[0].get("SC_CODE"), "500002")

    def test_parser_equity_fails(self):
        parser = EquityParser()
        companies_details = parser.parse("")
        self.assertEqual(companies_details.message,
                         ': file "" does not exist, or is not readable')

    def test_required_columns_missing(self):
        parser = EquityParser()
        try:
            parser.parse(ROOT_DIR + "/data/EQ261217_INVALID.CSV")
        except ValueError as e:
            err = e

        self.assertEqual(err.message, 'missing, required field')
