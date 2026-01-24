import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_single_character(self):
        self.assertEqual(sort_String("a"), "a")

    def test_sorted_string(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_unsorted_string(self):
        self.assertEqual(sort_String("olleh"), "ehllo")

    def test_string_with_spaces(self):
        self.assertEqual(sort_String("hello world"), " dehllorw")

    def test_string_with_punctuation(self):
        self.assertEqual(sort_String("Hello, world!"), ",!dehllorw")

    def test_string_with_numbers(self):
        self.assertEqual(sort_String("Hello123 world!"), "!123dehllorw")

    def test_string_with_special_characters(self):
        self.assertEqual(sort_String("Hello, world!@#"), "!@#dehllorw")
