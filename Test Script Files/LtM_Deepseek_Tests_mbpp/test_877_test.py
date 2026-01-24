import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_sorted_string(self):
        self.assertEqual(sort_String("abcdef"), "abcdef")

    def test_string_with_numbers(self):
        self.assertEqual(sort_String("123456"), "123456")

    def test_string_with_special_characters(self):
        self.assertEqual(sort_String("!@#$%^"), "!@#$%^")

    def test_string_with_mixed_case(self):
        self.assertEqual(sort_String("HeLlO"), "HelLO")

    def test_string_with_duplicate_characters(self):
        self.assertEqual(sort_String("aabbcc"), "aabbcc")
