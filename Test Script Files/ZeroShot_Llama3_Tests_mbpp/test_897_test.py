import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_present(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_absent(self):
        self.assertFalse(is_Word_Present("Hello World", "Python"))

    def test_present_with_uppercase(self):
        self.assertTrue(is_Word_Present("Hello World", "WORLD"))

    def test_absent_with_uppercase(self):
        self.assertFalse(is_Word_Present("Hello World", "PYTHON"))

    def test_present_with_punctuation(self):
        self.assertTrue(is_Word_Present("Hello, World!", "World"))

    def test_absent_with_punctuation(self):
        self.assertFalse(is_Word_Present("Hello, World!", "Python"))

    def test_present_with_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123 World", "World"))

    def test_absent_with_numbers(self):
        self.assertFalse(is_Word_Present("Hello 123 World", "Python"))
