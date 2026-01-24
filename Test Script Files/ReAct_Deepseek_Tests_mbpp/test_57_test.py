import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([5, 7, 9, 3, 6], 5), 97536)

    def test_single_digit_case(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_same_digits_case(self):
        self.assertEqual(find_Max_Num([5, 5, 5, 5], 4), 5555)

    def test_large_number_case(self):
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5, 4, 3, 2, 1], 9), 987654321)

    def test_negative_number_case(self):
        self.assertEqual(find_Max_Num([-1, -2, -3, -4, -5], 5), -12345)

    def test_zero_case(self):
        self.assertEqual(find_Max_Num([0, 0, 0, 0], 4), 0)

    def test_empty_array_case(self):
        with self.assertRaises(ValueError):
            find_Max_Num([], 0)

    def test_invalid_input_case(self):
        with self.assertRaises(TypeError):
            find_Max_Num("57_code", 5)
