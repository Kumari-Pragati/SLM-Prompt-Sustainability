import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Max_Num([1, 2, 3], 3), 321)

    def test_edge_case_empty(self):
        with self.assertRaises(IndexError):
            find_Max_Num([], 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Max_Num([5], 1), 5)

    def test_edge_case_max_value(self):
        self.assertEqual(find_Max_Num([9, 9, 9], 3), 999)

    def test_edge_case_min_value(self):
        self.assertEqual(find_Max_Num([1, 1, 1], 3), 111)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3], 3), -3)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(find_Max_Num([-1, 2, 3], 3), 321)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_Max_Num([1, 1, 1], 3), 111)

    def test_edge_case_zero(self):
        self.assertEqual(find_Max_Num([0, 0, 0], 3), 0)

    def test_edge_case_zero_and_non_zero(self):
        self.assertEqual(find_Max_Num([0, 1, 2], 3), 21)
