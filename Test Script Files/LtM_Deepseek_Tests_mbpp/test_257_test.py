import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_simple_swap(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_same_number_swap(self):
        self.assertEqual(swap_numbers(5, 5), (5, 5))

    def test_zero_swap(self):
        self.assertEqual(swap_numbers(0, 0), (0, 0))

    def test_negative_numbers_swap(self):
        self.assertEqual(swap_numbers(-1, -2), (-2, -1))

    def test_large_numbers_swap(self):
        self.assertEqual(swap_numbers(1000000, 2000000), (2000000, 1000000))

    def test_float_numbers_swap(self):
        self.assertEqual(swap_numbers(1.5, 2.5), (2.5, 1.5))

    def test_string_numbers_swap(self):
        with self.assertRaises(TypeError):
            swap_numbers("1", "2")

    def test_boolean_numbers_swap(self):
        with self.assertRaises(TypeError):
            swap_numbers(True, False)

    def test_none_numbers_swap(self):
        with self.assertRaises(TypeError):
            swap_numbers(None, None)
