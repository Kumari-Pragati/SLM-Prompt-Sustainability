import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_word(self):
        self.assertEqual(find_Max_Len_Even("hello"), "hello")

    def test_single_word_even_length(self):
        self.assertEqual(find_Max_Len_Even("world"), "world")

    def test_multiple_words_odd_length(self):
        self.assertEqual(find_Max_Len_Even("apple banana cherry"), "cherry")

    def test_multiple_words_even_length(self):
        self.assertEqual(find_Max_Len_Even("cat dog fish"), "fish")

    def test_multiple_words_mixed_length(self):
        self.assertEqual(find_Max_Len_Even("quick brown fox jumps over the lazy dog"), "lazy dog")

    def test_multiple_words_spaces_only(self):
        self.assertEqual(find_Max_Len_Even("   "), "   ")
