from unittest import TestCase
from services.equity_parser import EquityParser
from services.web_scraper import BseWebScraper


class WebScraperTest(TestCase):
    def test_csv_downloaded(self):
        bse = BseWebScraper()
        path_to_csv = bse.download_equity_csv()
        self.assertNotEqual(path_to_csv, None)
        parser = EquityParser()
        companies_details = parser.parse(path_to_csv)
        bse.delete_file(path_to_csv)
        self.assertEqual(set(companies_details[0].keys()), {'SC_CODE',
                                                            'SC_NAME',
                                                            'HIGH',
                                                            'LOW',
                                                            'CLOSE',
                                                            'OPEN'})
