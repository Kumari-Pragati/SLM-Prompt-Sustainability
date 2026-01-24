import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Max_Len_Even("this is a test"), "test")
        self.assertEqual(find_Max_Len_Even("even length string"), "")
        self.assertEqual(find_Max_Len_Even("  only spaces  "), " ")

    def test_edge_case_odd_length(self):
        self.assertEqual(find_Max_Len_Even("this is a test string"), "test string")
        self.assertEqual(find_Max_Len_Even("  only spaces and a trailing letter  "), " ")

    def test_edge_case_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_edge_case_single_char(self):
        self.assertEqual(find_Max_Len_Even("a"), "-1")

    def test_corner_case_mixed_even_odd(self):
        self.assertEqual(find_Max_Len_Even("this is a test string with an odd number of characters"), "test string with an odd number of characters")
