import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_Max_Num([], 0), 0)

    def test_single_digit_number(self):
        self.assertEqual(find_Max_Num([1], 1), 1)
        self.assertEqual(find_Max_Num([9], 1), 9)

    def test_multiple_digits_numbers(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 12345)
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5], 5), 98765)

    def test_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -3, -4, -5], 5), 54321)

    def test_mixed_numbers(self):
        self.assertEqual(find_Max_Num([1, -2, 3, -4, 5], 5), 153421)

    def test_long_list(self):
        long_list = [i for i in range(100000)]
        self.assertEqual(find_Max_Num(long_list, len(long_list)), int(str(long_list[-1]) * len(long_list)))

    def test_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            find_Max_Num((), 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            find_Max_Num([1, 2, 3], -1)
