import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_lowercase("Hello World"), "HW")
        self.assertEqual(remove_lowercase("hello world"), "HW")
        self.assertEqual(remove_lowercase("HELLO WORLD"), "HW")

    def test_empty(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_single_char(self):
        self.assertEqual(remove_lowercase("a"), "")
        self.assertEqual(remove_lowercase("A"), "")

    def test_multiple_chars(self):
        self.assertEqual(remove_lowercase("abc"), "")
        self.assertEqual(remove_lowercase("ABC"), "")

    def test_mixed_case(self):
        self.assertEqual(remove_lowercase("AbC"), "C")
        self.assertEqual(remove_lowercase("aBc"), "C")

    def test_non_ascii_chars(self):
        self.assertEqual(remove_lowercase("ä"), "")
        self.assertEqual(remove_lowercase("Ä"), "")
