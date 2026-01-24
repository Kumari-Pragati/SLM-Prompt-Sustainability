import unittest
from mbpp_906_code import datetime, timedelta
from 906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_typical_date_format(self):
        self.assertEqual(extract_date('/2022/01/01/'), [('2022', '01', '01')])
        self.assertEqual(extract_date('/2022/01/31/'), [('2022', '01', '31')])
        self.assertEqual(extract_date('/2022/12/25/'), [('2022', '12', '25')])

    def test_edge_cases_date_format(self):
        self.assertEqual(extract_date('/2022/01/00/'), [])
        self.assertEqual(extract_date('/2022/13/01/'), [])
        self.assertEqual(extract_date('/2022/00/01/'), [])
        self.assertEqual(extract_date('/2022/12/32/'), [])

    def test_edge_cases_year_format(self):
        self.assertEqual(extract_date('/0001/01/01/'), [])
        self.assertEqual(extract_date('/9999/01/01/'), [])

    def test_invalid_date_format(self):
        self.assertEqual(extract_date('/2022/32/01/'), [])
        self.assertEqual(extract_date('/2022/01/32/'), [])
        self.assertEqual(extract_date('/2022/01/01/32/'), [])

    def test_invalid_url_format(self):
        self.assertEqual(extract_date('/2022/01/01'), [])
        self.assertEqual(extract_date('/2022/01'), [])
        self.assertEqual(extract_date('/2022'), [])
        self.assertEqual(extract_date('/'), [])

    def test_date_out_of_range(self):
        self.assertEqual(extract_date('/2022/02/29/'), [('2022', '02', '29')])  # Feb 29 in leap years
        self.assertEqual(extract_date('/2021/02/29/'), [])
        self.assertEqual(extract_date('/2022/13/01/'), [])
        self.assertEqual(extract_date('/2022/00/01/'), [])
        self.assertEqual(extract_date('/2022/12/32/'), [])

    def test_date_from_future(self):
        self.assertEqual(extract_date('/3000/01/01/'), [])
        self.assertEqual(extract_date('/2023/12/31/23:59:59/'), [])  # 24 hours in a day
        self.assertEqual(extract_date('/2023/12/31/24:00:00/'), [])  # 24 hours in a day
