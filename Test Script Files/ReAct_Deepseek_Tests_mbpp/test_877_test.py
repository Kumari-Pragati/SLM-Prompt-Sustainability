import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_single_character(self):
        self.assertEqual(sort_String("a"), "a")

    def test_sorted_string(self):
        self.assertEqual(sort_String("abcdef"), "abcdef")

    def test_repeated_characters(self):
        self.assertEqual(sort_String("aabbcc"), "aabbcc")

    def test_numeric_string(self):
        self.assertEqual(sort_String("123456"), "123456")

    def test_special_characters(self):
        self.assertEqual(sort_String("!@#$%^"), "!@#$%^")

    def test_mixed_case(self):
        self.assertEqual(sort_String("HeLlO"), "HeLlO")

    def test_sorting_with_spaces(self):
        self.assertEqual(sort_String("hello world"), " dehllloorw")

    def test_sorting_with_numbers_and_letters(self):
        self.assertEqual(sort_String("abc123def"), "123abcdef")

    def test_sorting_with_special_characters_and_letters(self):
        self.assertEqual(sort_String("abc!@#def"), "!@#abcdef")
