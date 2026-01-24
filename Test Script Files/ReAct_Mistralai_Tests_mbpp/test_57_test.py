import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            find_Max_Num([], 0)

    def test_single_element(self):
        self.assertEqual(find_Max_Num([1], 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(find_Max_Num([1, 2, 9, 90, 900], 5), 90090)

    def test_negative_numbers(self):
        self.assertEqual(find_Max_Num([-1, -2, -9, -90, -900], 5), -90090)

    def test_zero(self):
        self.assertEqual(find_Max_Num([0], 1), 0)
        self.assertEqual(find_Max_Num([0, 0, 0], 3), 0)

    def test_long_list(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 90, 900, 9000, 90000], 12), 900009000)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            find_Max_Num([1, 'a', 2], 2)
