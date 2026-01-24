import unittest
from mbpp_749_code import sort_numeric_strings

class TestSortNumericStrings(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_numeric_strings([]), [])

    def test_single_element(self):
        self.assertEqual(sort_numeric_strings(['1']), ['1'])

    def test_multiple_elements(self):
        self.assertEqual(sort_numeric_strings(['5', '10', '1', '15', '3']), ['1', '3', '5', '10', '15'])

    def test_mixed_case(self):
        self.assertEqual(sort_numeric_strings(['FoO', '1', 'bAr', '42', 'ZePpInG']), ['1', '42', 'FoO', 'bAr', 'ZePpInG'])

    def test_leading_zeros(self):
        self.assertEqual(sort_numeric_strings(['001', '01', '1']), ['001', '01', '1'])

    def test_trailing_zeros(self):
        self.assertEqual(sort_numeric_strings(['1', '10', '100']), ['1', '10', '100'])

    def test_negative_numbers(self):
        self.assertEqual(sort_numeric_strings(['-1', '1', '-2', '3']), ['-2', '-1', '1', '3'])
