import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_swap_equal_numbers(self):
        self.assertEqual(swap_numbers(5, 5), (5, 5))

    def test_swap_normal_numbers(self):
        self.assertEqual(swap_numbers(3, 7), (7, 3))

    def test_swap_zero_numbers(self):
        self.assertEqual(swap_numbers(0, 0), (0, 0))

    def test_swap_negative_numbers(self):
        self.assertEqual(swap_numbers(-3, -7), (-7, -3))

    def test_swap_large_numbers(self):
        self.assertEqual(swap_numbers(1000, 2000), (2000, 1000))

    def test_swap_float_numbers(self):
        self.assertTupleEqual(swap_numbers(3.14, 2.71), (2.71, 3.14))

    def test_swap_string_numbers(self):
        self.assertTupleEqual(swap_numbers('5', '7'), ('7', '5'))

    def test_swap_invalid_inputs(self):
        self.assertRaises(TypeError, swap_numbers, 'a', 'b')
        self.assertRaises(TypeError, swap_numbers, 3, 'b')
