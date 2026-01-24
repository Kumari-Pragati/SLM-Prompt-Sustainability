import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(extract_date('https://example.com/2022/02/15'), [('2022', '02', '15')])

    def test_empty_input(self):
        self.assertIsNone(extract_date(''))

    def test_invalid_input(self):
        self.assertIsNone(extract_date('https://example.com/invalid'))

    def test_multiple_matches(self):
        self.assertEqual(extract_date('https://example.com/2022/02/15/2023/03/16'), [('2022', '02', '15'), ('2023', '03', '16')])

    def test_single_match(self):
        self.assertEqual(extract_date('https://example.com/2022/02/15/'), [('2022', '02', '15')])

    def test_no_match(self):
        self.assertIsNone(extract_date('https://example.com'))
