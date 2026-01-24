import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):
    def test_valid_date_format(self):
        self.assertEqual(extract_date('/2022/01/01/'), [('2022', '01', '01')])
        self.assertEqual(extract_date('/2022/01/31/'), [('2022', '01', '31')])
        self.assertEqual(extract_date('/2022/12/31/'), [('2022', '12', '31')])

    def test_invalid_date_format(self):
        self.assertIsNone(extract_date('/2022/01/32/'))
        self.assertIsNone(extract_date('/2022/13/01/'))
        self.assertIsNone(extract_date('/2022/01/00/'))
        self.assertIsNone(extract_date('/2022/00/01/'))
        self.assertIsNone(extract_date('/2022/01/'))
        self.assertIsNone(extract_date('/2022/'))
        self.assertIsNone(extract_date('/'))
