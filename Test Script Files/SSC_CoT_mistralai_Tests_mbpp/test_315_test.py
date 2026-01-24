import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Max_Len_Even("this is a test"), "test")
        self.assertEqual(find_Max_Len_Even("even length string"), "")
        self.assertEqual(find_Max_Len_Even("  only spaces  "), "  ")

    def test_edge_cases(self):
        self.assertEqual(find_Max_Len_Even("a"), "")
        self.assertEqual(find_Max_Len_Even("aa"), "a")
        self.assertEqual(find_Max_Len_Even("   "), "")
        self.assertEqual(find_Max_Len_Even("   a   "), "a")
        self.assertEqual(find_Max_Len_Even("  a   b   "), "b")

    def test_boundary_cases(self):
        self.assertEqual(find_Max_Len_Even("a b"), "b")
        self.assertEqual(find_Max_Len_Even("a   b"), "b")
        self.assertEqual(find_Max_Len_Even("a b   "), "b")
        self.assertEqual(find_Max_Len_Even(" a   b  "), "b")
        self.assertEqual(find_Max_Len_Even(" a   b   "), "b")

    def test_invalid_inputs(self):
        self.assertEqual(find_Max_Len_Even(123), "-1")
        self.assertEqual(find_Max_Len_Even([]), "-1")
        self.assertEqual(find_Max_Len_Even(None), "-1")
        self.assertEqual(find_Max_Len_Even("1a"), "-1")
        self.assertEqual(find_Max_Len_Even("a1"), "-1")
