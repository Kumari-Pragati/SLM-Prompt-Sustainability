import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_upper("HELLO"))

    def test_edge_case_uppercase_only(self):
        self.assertTrue(is_upper("A"))

    def test_edge_case_lowercase_only(self):
        self.assertFalse(is_upper("hello"))

    def test_edge_case_mixed_case(self):
        self.assertFalse(is_upper("HeLlo"))

    def test_empty_string(self):
        self.assertTrue(is_upper(""))

    def test_whitespace_string(self):
        self.assertTrue(is_upper("   "))

    def test_non_string_input(self):
        self.assertRaises(TypeError, is_upper, 123)
