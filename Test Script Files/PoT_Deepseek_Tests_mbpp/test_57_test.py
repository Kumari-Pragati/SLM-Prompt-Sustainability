import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Max_Num([5], 1), 5)

    def test_boundary_case_empty_array(self):
        self.assertEqual(find_Max_Num([], 0), None)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(find_Max_Num([5, 5, 5, 5], 4), 5555)

    def test_corner_case_large_numbers(self):
        self.assertEqual(find_Max_Num([9, 9, 9, 9, 9], 5), 99999)

    def test_corner_case_small_numbers(self):
        self.assertEqual(find_Max_Num([0, 0, 0, 0, 0], 5), 0)

    def test_invalid_input_negative_numbers(self):
        with self.assertRaises(Exception):
            find_Max_Num([-1, -2, -3, -4, -5], 5)

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(Exception):
            find_Max_Num([1, 2, '3', 4, 5], 5)
