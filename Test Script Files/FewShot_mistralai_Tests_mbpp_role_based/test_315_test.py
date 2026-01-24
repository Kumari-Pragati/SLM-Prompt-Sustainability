import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_word(self):
        self.assertEqual(find_Max_Len_Even("even"), "even")

    def test_single_odd_word(self):
        self.assertEqual(find_Max_Len_Even("odd"), "-1")

    def test_multiple_even_words(self):
        self.assertEqual(find_Max_Len_Even("even even even"), "even even even")

    def test_multiple_odd_words(self):
        self.assertEqual(find_Max_Len_Even("odd odd odd"), "-1")

    def test_mixed_words(self):
        self.assertEqual(find_Max_Len_Even("even odd even"), "even")

    def test_long_even_string(self):
        self.assertEqual(find_Max_Len_Even("even even even even even"), "even even even even even")

    def test_long_odd_string(self):
        self.assertEqual(find_Max_Len_Even("odd odd odd odd odd"), "-1")

    def test_string_with_leading_space(self):
        self.assertEqual(find_Max_Len_Even(" even even"), "even even")

    def test_string_with_trailing_space(self):
        self.assertEqual(find_Max_Len_Even("even even "), "even even")

    def test_string_with_spaces_in_middle(self):
        self.assertEqual(find_Max_Len_Even("even even   even"), "even even even")
