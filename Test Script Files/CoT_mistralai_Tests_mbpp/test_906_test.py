import unittest
from mbpp_906_code import datetime, dates
from 906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_valid_date_format(self):
        self.assertListEqual(extract_date('/2022/01/01/'), [('2022', '01', '01')])
        self.assertListEqual(extract_date('/2022/01/31/'), [('2022', '01', '31')])
        self.assertListEqual(extract_date('/2022/12/31/'), [('2022', '12', '31')])
        self.assertListEqual(extract_date('/2022/02/29/'), [('2022', '02', '29')])  # Leap year

    def test_invalid_date_format(self):
        self.assertListEqual(extract_date('/2022/00/01/'), [])
        self.assertListEqual(extract_date('/2022/13/01/'), [])
        self.assertListEqual(extract_date('/2022/01/32/'), [])
        self.assertListEqual(extract_date('/2022/01/00/'), [])
        self.assertListEqual(extract_date('/2022/01/'), [])
        self.assertListEqual(extract_date('/2022/'), [])
        self.assertListEqual(extract_date('/'), [])

    def test_invalid_year(self):
        self.assertListEqual(extract_date('/0/01/01/'), [])
        self.assertListEqual(extract_date('/9999/01/01/'), [])
        self.assertListEqual(extract_date('/0000/01/01/'), [])
        self.assertListEqual(extract_date('/-1/01/01/'), [])
        self.assertListEqual(extract_date('/2022/00/01/'), [])
        self.assertListEqual(extract_date('/2022/-1/01/'), [])
        self.assertListEqual(extract_date('/2022/2022/01/'), [])

    def test_empty_string(self):
        self.assertListEqual(extract_date(''), [])

    def test_date_in_middle_of_url(self):
        self.assertListEqual(extract_date('/some/text/2022/01/01/more/text/'), [('2022', '01', '01')])

    def test_date_at_beginning_of_url(self):
        self.assertListEqual(extract_date('/2022/01/01/some/text/'), [('2022', '01', '01')])

    def test_date_at_end_of_url(self):
        self.assertListEqual(extract_date('/some/text/2022/01/01/'), [('2022', '01', '01')])
