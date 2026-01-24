import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_edge_cases(self):
        self.assertEqual(swap_numbers(-1, 0), (0, -1))
        self.assertEqual(swap_numbers(0, 0), (0, 0))

    def test_swap_between_negative_numbers(self):
        self.assertEqual(swap_numbers(-1, -2), (-2, -1))

    def test_swap_between_zero_and_negative_numbers(self):
        self.assertEqual(swap_numbers(0, -1), (-1, 0))

    def test_swap_between_positive_and_negative_numbers(self):
        self.assertEqual(swap_numbers(1, -2), (-2, 1))

    def test_swap_between_positive_numbers(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_swap_between_zero_and_positive_numbers(self):
        self.assertEqual(swap_numbers(0, 1), (1, 0))

    def test_swap_between_positive_and_zero_numbers(self):
        self.assertEqual(swap_numbers(1, 0), (0, 1))

    def test_swap_between_zero_and_positive_numbers(self):
        self.assertEqual(swap_numbers(0, 2), (2, 0))
