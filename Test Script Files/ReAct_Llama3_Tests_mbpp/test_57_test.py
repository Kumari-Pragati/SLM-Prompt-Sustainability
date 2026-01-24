import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)

    def test_edge_case_single_digit(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_edge_case_zero(self):
        self.assertRaises(IndexError, find_Max_Num, [], 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3, -4, -5], 5), -54321)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_Max_Num([1, 2, 2, 3, 4, 5], 6), 54321)

    def test_edge_case_empty_array(self):
        self.assertRaises(IndexError, find_Max_Num, [], 0)

    def test_edge_case_array_with_one_element(self):
        self.assertEqual(find_Max_Num([1], 1), 1)
