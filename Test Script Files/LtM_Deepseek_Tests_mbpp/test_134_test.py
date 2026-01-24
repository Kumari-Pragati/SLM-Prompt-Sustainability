import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_simple_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "ODD")

    def test_simple_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "EVEN")

    def test_empty_array(self):
        self.assertEqual(check_last([], 0, 1), "EVEN")

    def test_single_element_array(self):
        self.assertEqual(check_last([5], 1, 1), "ODD")

    def test_negative_numbers(self):
        self.assertEqual(check_last([-1, -2, -3, -4], 4, 1), "EVEN")

    def test_large_numbers(self):
        self.assertEqual(check_last([1000000000, 2000000000, 3000000000, 4000000000], 4, 1), "ODD")

    def test_p_not_equal_to_1(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 0), "EVEN")
