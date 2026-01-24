import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_lower("hello"))

    def test_edge_case_uppercase(self):
        self.assertTrue(is_lower("HeLlO"))

    def test_edge_case_empty_string(self):
        self.assertTrue(is_lower(""))

    def test_edge_case_whitespace(self):
        self.assertTrue(is_lower("\t\n "))

    def test_corner_case_numbers(self):
        self.assertFalse(is_lower("123"))

    def test_corner_case_special_characters(self):
        self.assertFalse(is_lower("!@#$%^&*()"))
