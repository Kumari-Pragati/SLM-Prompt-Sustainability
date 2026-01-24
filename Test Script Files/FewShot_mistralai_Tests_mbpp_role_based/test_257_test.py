import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_swapping_positive_numbers(self):
        self.assertEqual(swap_numbers(2, 3), (3, 2))

    def test_swapping_zero_and_positive_number(self):
        self.assertEqual(swap_numbers(0, 3), (3, 0))

    def test_swapping_negative_numbers(self):
        self.assertEqual(swap_numbers(-2, -3), (-3, -2))

    def test_swapping_same_numbers(self):
        self.assertEqual(swap_numbers(2, 2), (2, 2))
