import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([5, 7, 9, 3, 6], 5), 97536)

    def test_single_digit(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_same_digits(self):
        self.assertEqual(find_Max_Num([9, 9, 9, 9, 9], 5), 99999)

    def test_reverse_order(self):
        self.assertEqual(find_Max_Num([9, 8, 7, 6, 5], 5), 98765)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Max_Num("57_code", 5)

        with self.assertRaises(TypeError):
            find_Max_Num([5, 7, 9, 3, 6], "5")

        with self.assertRaises(ValueError):
            find_Max_Num([5, 7, 9, 3, 6], -1)

        with self.assertRaises(ValueError):
            find_Max_Num([5, 7, 9, 3, 6], 0)
