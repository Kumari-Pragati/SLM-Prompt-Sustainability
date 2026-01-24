import unittest
from mbpp_906_code import datetime
from 906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_valid_date_format(self):
        self.assertEqual(extract_date('/2022/01/01/'), [('2022', '01', '01')])
        self.assertEqual(extract_date('/2022/01/31/'), [('2022', '01', '31')])
        self.assertEqual(extract_date('/2022/12/31/'), [('2022', '12', '31')])

    def test_invalid_date_format(self):
        self.assertIsNone(extract_date('/2022/01/32/'))
        self.assertIsNone(extract_date('/2022/13/01/'))
        self.assertIsNone(extract_date('/2022/01/00/'))
        self.assertIsNone(extract_date('/2022/01/'))
        self.assertIsNone(extract_date('/2022/'))
        self.assertIsNone(extract_date('/'))

    def test_empty_string(self):
        self.assertIsNone(extract_date(''))

    def test_date_string_with_extra_slashes(self):
        self.assertIsNone(extract_date('/2022//01/01//'))

    def test_date_string_with_extra_characters(self):
        self.assertIsNone(extract_date('/2022a/01/01/'))
        self.assertIsNone(extract_date('/2022/01b/01/'))
        self.assertIsNone(extract_date('/2022/01/01c/'))

    def test_date_string_with_missing_slashes(self):
        self.assertIsNone(extract_date('/20220101'))
        self.assertIsNone(extract_date('/2022/0101/'))
        self.assertIsNone(extract_date('/2022/01/010/'))

    def test_date_string_with_extra_numbers(self):
        self.assertIsNone(extract_date('/2022/01/019/'))

    def test_date_string_with_year_out_of_range(self):
        self.assertIsNone(extract_date('/0001/01/01/'))
        self.assertIsNone(extract_date('/9999/01/01/'))
        self.assertIsNone(extract_date('/2023/13/01/'))
        self.assertIsNone(extract_date('/2022/00/01/'))
        self.assertIsNone(extract_date('/2022/12/32/'))

    def test_date_string_with_month_out_of_range(self):
        self.assertIsNone(extract_date('/2022/00/01/'))
        self.assertIsNone(extract_date('/2022/13/01/'))
        self.assertIsNone(extract_date('/2022/02/31/'))
        self.assertIsNone(extract_date('/2022/12/32/'))
