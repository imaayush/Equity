import os
from .constants import FIELDS_NAMES


class EquityParser():
    """Take .csv file path as input and return list of dic"""

    def _is_readable_file(self, path):
        return os.path.isfile(path) and os.access(path, os.R_OK)

    def __init__(self):
        self.column_names = FIELDS_NAMES
        self.erros = {}

    def _covert_line_into_dic(self, line, column_names_with_index):
        """Input is line and cloumn names with its index convert it into dic
           Ex:
             Input: 500002,ABB LTD.,A ,Q,1389.00,1399.90,1374.15,1391.05,1391.05,1378.05,321,95555,132897086.00,
             Output: {"SC_CODE: 500002, "SC_NAME": "ABB LTD.",
                      "OPEN":1393.45, "HIGH":1433.40, "LOW": 1383.85,
                      "CLOSE": 1388.15}
        """
        company_raw_details = line.split(',')
        company_details = {}
        for key, value in column_names_with_index.iteritems():
            company_details[key] = company_raw_details[value].strip()

        return company_details

    def _find_company_columns_with_index(self, columns_in_file):
        """find position of cloumn name
           Ex:
            Input: SC_CODE,SC_NAME,SC_GROUP,SC_TYPE,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,NO_TRADES,NO_OF_SHRS,NET_TURNOV,TDCLOINDI
            Ouput:{"SC_CODE: 0, "SC_NAME": 1,
                    "OPEN":4, "HIGH":5, "LOW": 6,
                    "CLOSE": 7}
           """
        column_names_with_index = {}
        for index_num in range(0, len(columns_in_file)):
            if columns_in_file[index_num] in self.column_names:
                column_names_with_index[columns_in_file[index_num]] = index_num

        return column_names_with_index

    def parse(self, path):
        """Take .csv file path as input and return list of dic"""
        companies_details = []

        if not self._is_readable_file(path):
            return ValueError(
                '{}: file "{}" does not exist, or is not readable'.format(path,
                                                                          path)
            )
        with open(path, "rb") as finput:
            self.lines = finput.read().split('\n')
            column_names_with_index = self._find_company_columns_with_index(
                self.lines[0].split(','))

            companies_details = []

            for line in self.lines[1:]:
                if line:
                    companies_details.append(self._covert_line_into_dic(
                        line, column_names_with_index))

        return companies_details
