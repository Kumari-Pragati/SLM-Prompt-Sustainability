import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_simple_upper(self):
        self.assertTrue(is_upper("UPPER"))
    def test_simple_lower(self):
        self.assertFalse(is_upper("lower"))
    def test_empty_string(self):
        self.assertFalse(is_upper(""))
    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_upper(123)
    def test_mixed_case(self):
        self.assertTrue(is_upper("mIxEd"))
    def test_all_upper(self):
        self.assertTrue(is_upper("ALLUPPER"))
    def test_all_lower(self):
        self.assertFalse(is_upper("ALLLOWER"))
