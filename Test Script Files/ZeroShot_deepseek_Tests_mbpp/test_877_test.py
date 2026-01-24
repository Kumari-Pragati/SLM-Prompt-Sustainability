import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_sort_string_with_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_sort_string_with_single_character(self):
        self.assertEqual(sort_String("a"), "a")

    def test_sort_string_with_multiple_characters(self):
        self.assertEqual(sort_String("cba"), "abc")

    def test_sort_string_with_duplicate_characters(self):
        self.assertEqual(sort_String("cabba"), "ababc")

    def test_sort_string_with_special_characters(self):
        self.assertEqual(sort_String("abc!@#"), "!@#abc")

    def test_sort_string_with_numbers_and_letters(self):
        self.assertEqual(sort_String("abc123"), "123abc")
