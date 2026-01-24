import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_find_max_num_empty_list(self):
        self.assertEqual(find_Max_Num([], 0), 0)

    def test_find_max_num_single_element(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_find_max_num_multiple_elements(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)

    def test_find_max_num_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3, -4, -5], 5), 54321)

    def test_find_max_num_zero(self):
        self.assertEqual(find_Max_Num([0], 1), 0)
        self.assertEqual(find_Max_Num([0, 0, 0], 3), 000)

    def test_find_max_num_long_list(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1], 20), 1908455369)
