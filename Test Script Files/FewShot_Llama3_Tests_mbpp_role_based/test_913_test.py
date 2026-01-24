import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertTrue(end_num("hello123"))

    def test_negative_integer(self):
        self.assertTrue(end_num("-123"))

    def test_zero(self):
        self.assertTrue(end_num("0"))

    def test_non_numeric_string(self):
        self.assertFalse(end_num("hello"))

    def test_empty_string(self):
        self.assertFalse(end_num(""))

    def test_string_with_non_numeric_characters(self):
        self.assertFalse(end_num("helloabc"))

    def test_string_with_non_numeric_characters_at_end(self):
        self.assertTrue(end_num("helloabc123"))

    def test_string_with_non_numeric_characters_in_middle(self):
        self.assertFalse(end_num("hello123abc"))
