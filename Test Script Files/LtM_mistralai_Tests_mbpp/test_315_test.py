import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_simple_even_length(self):
        self.assertEqual(find_Max_Len_Even("this is a test"), "test")
        self.assertEqual(find_Max_Len_Even("a b c d e"), "c d e")

    def test_simple_odd_length(self):
        self.assertEqual(find_Max_Len_Even("this is a test "), "-1")
        self.assertEqual(find_Max_Len_Even("a b c d e "), "-1")

    def test_edge_cases(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")
        self.assertEqual(find_Max_Len_Even(" "), "-1")
        self.assertEqual(find_Max_Len_Even("a"), "-1")
        self.assertEqual(find_Max_Len_Even(" a"), "-1")
        self.assertEqual(find_Max_Len_Even(" a "), "-1")

    def test_boundary_cases(self):
        self.assertEqual(find_Max_Len_Even("a b c d e f"), "c d e f")
        self.assertEqual(find_Max_Len_Even("a b c d e f g"), "c d e f g")
        self.assertEqual(find_Max_Len_Even("a b c d e f g h"), "c d e f g h")
        self.assertEqual(find_Max_Len_Even("a b c d e f g h i"), "c d e f g h i")

    def test_complex_cases(self):
        self.assertEqual(find_Max_Len_Even("this is a test with spaces in between"), "test with spaces in between")
        self.assertEqual(find_Max_Len_Even("this is a test with spaces in between and at the beginning and end"), "test with spaces in between")
