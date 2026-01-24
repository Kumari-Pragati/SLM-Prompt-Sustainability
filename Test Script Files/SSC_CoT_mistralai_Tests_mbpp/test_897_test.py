import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(is_Word_Present("Hello World", "Hello"))
        self.assertTrue(is_Word_Present("Python is fun", "Python"))

    def test_edge_case(self):
        self.assertTrue(is_Word_Present("", ""))
        self.assertFalse(is_Word_Present("", "Word"))
        self.assertFalse(is_Word_Present("Word", ""))
        self.assertFalse(is_Word_Present("   Word   ", "Word"))
        self.assertTrue(is_Word_Present("Word", "Word "))
        self.assertTrue(is_Word_Present("Word", "Word\n"))
        self.assertTrue(is_Word_Present("Word", "Word,"))
        self.assertTrue(is_Word_Present("Word", "Word."))

    def test_special_cases(self):
        self.assertFalse(is_Word_Present("Hello World", "world"))
        self.assertFalse(is_Word_Present("Python is fun", "python"))
        self.assertFalse(is_Word_Present("Python is fun", "is fun"))
        self.assertFalse(is_Word_Present("Python is fun", "Python is"))
        self.assertFalse(is_Word_Present("Python is fun", "Python, is fun"))
        self.assertFalse(is_Word_Present("Python is fun", "Python is fun!"))
        self.assertFalse(is_Word_Present("Python is fun", "Python is fun\t"))
        self.assertFalse(is_Word_Present("Python is fun", "Python is fun\n\n"))
