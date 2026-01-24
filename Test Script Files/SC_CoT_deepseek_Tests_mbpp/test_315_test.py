import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Len_Even("This is a test string"), "is")

    def test_edge_case_with_single_word(self):
        self.assertEqual(find_Max_Len_Even("single"), "single")

    def test_edge_case_with_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_corner_case_with_all_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("even even even"), "even")

    def test_corner_case_with_all_odd_length_words(self):
        self.assertEqual(find_Max_Len_Even("odd odd odd odd"), "-1")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Max_Len_Even(12345)
