import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)

    def test_odd_count_even(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 2)

    def test_odd_count_odd(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9, 11], 6), 1)

    def test_single_element(self):
        self.assertEqual(min_Num([1], 1), 2)

    def test_all_even(self):
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)

    def test_empty_array(self):
        self.assertEqual(min_Num([], 0), 2)

    def test_negative_numbers(self):
        self.assertEqual(min_Num([-1, -3, -5, -7, -9], 5), 2)

    def test_mixed_numbers(self):
        self.assertEqual(min_Num([1, 2, -3, -4, 5], 5), 2)
