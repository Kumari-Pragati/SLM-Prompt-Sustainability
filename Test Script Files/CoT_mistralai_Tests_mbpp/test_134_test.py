import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_check_last_odd_sum(self):
        self.assertEqual(check_last([1, 3, 5], 3, 1), "ODD")
        self.assertEqual(check_last([1, 3, 5, 7], 4, 1), "ODD")
        self.assertEqual(check_last([1, 3, 5, 7, 9], 5, 1), "ODD")

    def test_check_last_even_sum(self):
        self.assertEqual(check_last([2, 4, 6], 3, 1), "EVEN")
        self.assertEqual(check_last([2, 4, 6, 8], 4, 1), "EVEN")
        self.assertEqual(check_last([2, 4, 6, 8, 10], 5, 1), "EVEN")

    def test_check_last_empty_list(self):
        self.assertEqual(check_last([], 0, 1), "EVEN")

    def test_check_last_single_element(self):
        self.assertEqual(check_last([1], 1, 1), "ODD")
        self.assertEqual(check_last([2], 1, 1), "EVEN")

    def test_check_last_negative_numbers(self):
        self.assertEqual(check_last([-1, -3, -5], 3, 1), "ODD")
        self.assertEqual(check_last([-2, -4, -6], 3, 1), "EVEN")

    def test_check_last_zero(self):
        self.assertEqual(check_last([0], 1, 1), "EVEN")

    def test_check_last_non_integer_elements(self):
        self.assertRaises(TypeError, check_last, [1.5, 3, 5], 3, 1)
        self.assertRaises(TypeError, check_last, [1, "three", 5], 3, 1)
        self.assertRaises(TypeError, check_last, [1, 3, "five"], 3, 1)
