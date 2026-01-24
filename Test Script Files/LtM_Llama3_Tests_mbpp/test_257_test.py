import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_simple_swap(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_swap_with_negative_numbers(self):
        self.assertEqual(swap_numbers(-1, 2), (-1, 2))

    def test_swap_with_zero(self):
        self.assertEqual(swap_numbers(0, 2), (2, 0))

    def test_swap_with_large_numbers(self):
        self.assertEqual(swap_numbers(100, 200), (200, 100))

    def test_swap_with_negative_large_numbers(self):
        self.assertEqual(swap_numbers(-100, -200), (-200, -100))

    def test_swap_with_equal_numbers(self):
        self.assertEqual(swap_numbers(1, 1), (1, 1))

    def test_swap_with_non_integer_numbers(self):
        self.assertEqual(swap_numbers(1.5, 2.5), (2.5, 1.5))

    def test_swap_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            swap_numbers('a', 'b')
