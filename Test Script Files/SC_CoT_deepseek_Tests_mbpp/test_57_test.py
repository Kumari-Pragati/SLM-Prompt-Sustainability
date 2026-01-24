import unittest

from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4], 4), 4231)

    def test_single_digit(self):
        self.assertEqual(find_Max_Num([5], 1), 5)

    def test_multiple_same_numbers(self):
        self.assertEqual(find_Max_Num([7, 7, 7], 3), 777)

    def test_large_numbers(self):
        self.assertEqual(find_Max_Num([9, 8, 7, 6], 4), 9876)

    def test_reverse_sorted_array(self):
        self.assertEqual(find_Max_Num([9, 8, 7, 6], 4), 9876)

    def test_small_numbers(self):
        self.assertEqual(find_Max_Num([0, 1, 2, 3], 4), 3210)

    def test_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3, -4], 4), -1234)

    def test_mixed_numbers(self):
        self.assertEqual(find_Max_Num([-1, 0, 1, 2], 4), 2101)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            find_Max_Num([], 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Max_Num("1234", 4)
