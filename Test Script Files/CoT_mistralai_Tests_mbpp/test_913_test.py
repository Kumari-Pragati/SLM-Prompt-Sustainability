import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_end_num_positive(self):
        self.assertTrue(end_num("Hello123"))
        self.assertTrue(end_num("123456789"))
        self.assertTrue(end_num("abcd1234"))

    def test_end_num_negative(self):
        self.assertFalse(end_num("Hello"))
        self.assertFalse(end_num("12345678"))
        self.assertFalse(end_num("abcd"))

    def test_empty_string(self):
        self.assertFalse(end_num(""))

    def test_only_spaces(self):
        self.assertFalse(end_num("   "))

    def test_special_characters(self):
        self.assertFalse(end_num("Hello@123"))
        self.assertFalse(end_num("123$%&"))
