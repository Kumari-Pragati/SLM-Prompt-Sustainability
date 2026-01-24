import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_same_number(self):
        self.assertEqual(swap_numbers(5, 5), (5, 5))

    def test_zero_numbers(self):
        self.assertEqual(swap_numbers(0, 0), (0, 0))

    def test_negative_numbers(self):
        self.assertEqual(swap_numbers(-1, -2), (-2, -1))

    def test_large_numbers(self):
        self.assertEqual(swap_numbers(1000000, 2000000), (2000000, 1000000))

    def test_non_integer_numbers(self):
        self.assertEqual(swap_numbers(1.5, 2.5), (2.5, 1.5))

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            swap_numbers("1", "2")

    def test_boolean_numbers(self):
        with self.assertRaises(TypeError):
            swap_numbers(True, False)

    def test_none_numbers(self):
        with self.assertRaises(TypeError):
            swap_numbers(None, None)
