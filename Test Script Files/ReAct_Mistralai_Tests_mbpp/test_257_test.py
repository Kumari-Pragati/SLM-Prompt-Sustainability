import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_swap_positive_numbers(self):
        self.assertTupleEqual(swap_numbers(5, 3), (3, 5))
        self.assertTupleEqual(swap_numbers(100, 200), (200, 100))

    def test_swap_zero_and_non_zero_numbers(self):
        self.assertTupleEqual(swap_numbers(0, 5), (5, 0))
        self.assertTupleEqual(swap_numbers(-10, 0), (0, -10))

    def test_swap_same_numbers(self):
        self.assertTupleEqual(swap_numbers(5, 5), (5, 5))

    def test_swap_negative_numbers(self):
        self.assertTupleEqual(swap_numbers(-5, -3), (-3, -5))
        self.assertTupleEqual(swap_numbers(-100, -200), (-200, -100))

    def test_swap_large_numbers(self):
        large_num = 1000000000000000000
        self.assertTupleEqual(swap_numbers(large_num, large_num * 2), (large_num * 2, large_num))
