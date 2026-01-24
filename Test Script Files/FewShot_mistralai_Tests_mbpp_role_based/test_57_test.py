import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)
        self.assertEqual(find_Max_Num([6, 7, 8, 9, 0], 5), 98760)
        self.assertEqual(find_Max_Num([10, 11, 12, 13, 14], 5), 14131210)

    def test_empty_list(self):
        self.assertIsNone(find_Max_Num([], 0))

    def test_single_element(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3, -4, -5], 5), 54321)

    def test_zero_numbers(self):
        self.assertEqual(find_Max_Num([0, 0, 0, 0, 0], 5), 0)

    def test_invalid_input_length(self):
        self.assertRaises(IndexError, find_Max_Num, [1, 2, 3], 4)

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, find_Max_Num, [1, 2, 3], 'a')
