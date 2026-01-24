import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_single_character_string(self):
        self.assertEqual(sort_String("a"), "a")

    def test_multiple_characters_string(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_string_with_spaces(self):
        self.assertEqual(sort_String("hello world"), " dehllorw")

    def test_string_with_punctuation(self):
        self.assertEqual(sort_String("Hello, world!"), ",dehllow!")

    def test_string_with_uppercase_and_lowercase(self):
        self.assertEqual(sort_String("Hello, world! ABC"), ",ABCdehllow!")

    def test_string_with_non_ascii_characters(self):
        self.assertEqual(sort_String("Hello, world! ABC à"), ",ABCàdehllow!")
