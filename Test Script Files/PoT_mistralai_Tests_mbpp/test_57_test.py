import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)
        self.assertEqual(find_Max_Num([6, 7, 8, 9, 0], 5), 67890)
        self.assertEqual(find_Max_Num([10, 11, 12, 13, 14], 5), 1011121314)

    def test_edge_case_single_digit(self):
        self.assertEqual(find_Max_Num([9], 1), 9)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Max_Num([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3], 3), -321)

    def test_corner_case_zero(self):
        self.assertEqual(find_Max_Num([0], 1), 0)
