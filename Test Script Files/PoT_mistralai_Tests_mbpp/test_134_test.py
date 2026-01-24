import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_typical_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 0), "EVEN")
        self.assertEqual(check_last([5, 6, 7, 8], 4, 0), "EVEN")

    def test_typical_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "ODD")
        self.assertEqual(check_last([5, 6, 7, 8], 4, 1), "ODD")

    def test_empty_list(self):
        self.assertEqual(check_last([], 0, 0), "EVEN")
        self.assertEqual(check_last([], 0, 1), "ODD")

    def test_single_element(self):
        self.assertEqual(check_last([1], 1, 0), "EVEN")
        self.assertEqual(check_last([1], 1, 1), "ODD")

    def test_negative_numbers(self):
        self.assertEqual(check_last([-1, 2, -3, 4], 4, 0), "EVEN")
        self.assertEqual(check_last([-1, 2, -3, 4], 4, 1), "ODD")
