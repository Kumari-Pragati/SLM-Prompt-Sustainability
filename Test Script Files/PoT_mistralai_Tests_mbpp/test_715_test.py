import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(str_to_tuple('1, 2, 3, 4'), (1, 2, 3, 4))

    def test_edge_case_empty_string(self):
        self.assertEqual(str_to_tuple(''), ())

    def test_edge_case_single_element(self):
        self.assertEqual(str_to_tuple('1'), (1,))

    def test_edge_case_single_comma(self):
        self.assertEqual(str_to_tuple('1, '), (1,))

    def test_edge_case_multiple_commas(self):
        self.assertEqual(str_to_tuple('1,,3'), (1, None, 3))

    def test_edge_case_trailing_comma(self):
        self.assertEqual(str_to_tuple('1, 2, 3, '), (1, 2, 3, None))

    def test_edge_case_leading_whitespace(self):
        self.assertEqual(str_to_tuple('  1, 2, 3'), (1, 2, 3))

    def test_edge_case_trailing_whitespace(self):
        self.assertEqual(str_to_tuple('1, 2, 3 '), (1, 2, 3))

    def test_edge_case_non_numeric_characters(self):
        self.assertRaises(ValueError, str_to_tuple, '1a, 2b, 3c')
