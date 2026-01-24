import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Len_Even("This is a test string"), "is")

    def test_edge_case_single_word(self):
        self.assertEqual(find_Max_Len_Even("string"), "string")

    def test_boundary_case_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_corner_case_all_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("one two three four"), "four")

    def test_corner_case_all_odd_length_words(self):
        self.assertEqual(find_Max_Len_Even("one two three four five"), "five")

    def test_corner_case_no_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("odd odd odd odd"), "-1")

    def test_corner_case_multiple_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("even length words even length"), "even length words")
