import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_typical_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 0), "EVEN")

    def test_typical_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "ODD")

    def test_empty_list(self):
        self.assertEqual(check_last([], 0, 0), "Error: List is empty")

    def test_single_element(self):
        self.assertEqual(check_last([1], 1, 0), "EVEN")
        self.assertEqual(check_last([1], 1, 1), "ODD")

    def test_negative_numbers(self):
        self.assertEqual(check_last([-1, 2, -3, 4], 4, 0), "EVEN")
        self.assertEqual(check_last([-1, 2, -3, 4], 4, 1), "ODD")

    def test_negative_sum(self):
        self.assertEqual(check_last([-1, -2, -3, -4], 4, 0), "EVEN")
        self.assertEqual(check_last([-1, -2, -3, -4], 4, 1), "ODD")
