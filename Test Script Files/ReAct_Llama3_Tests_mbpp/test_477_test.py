import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_lower(self):
        self.assertTrue(is_lower("hello"))
    def test_upper(self):
        self.assertFalse(is_lower("HELLO"))
    def test_mixed(self):
        self.assertTrue(is_lower("HeLlO"))
    def test_empty(self):
        self.assertFalse(is_lower(""))
    def test_single_char(self):
        self.assertTrue(is_lower("a"))
    def test_spaces(self):
        self.assertFalse(is_lower("   "))
    def test_punctuation(self):
        self.assertTrue(is_lower("Hello!"))
