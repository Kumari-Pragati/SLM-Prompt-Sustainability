import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_values_string("abcdefg"), "acfg")

    def test_edge_case_even_length(self):
        self.assertEqual(odd_values_string("ab"), "a")

    def test_edge_case_odd_length(self):
        self.assertEqual(odd_values_string("a"), "a")
        self.assertEqual(odd_values_string(""), "")

    def test_boundary_case_first_index(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_boundary_case_last_index(self):
        self.assertEqual(odd_values_string("abc"), "b")

    def test_corner_case_empty_string(self):
        self.assertEqual(odd_values_string(""), "")
