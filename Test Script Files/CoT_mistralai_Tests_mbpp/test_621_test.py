import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(increment_numerics([], 3), [])

    def test_single_digit(self):
        self.assertEqual(increment_numerics([1], 3), [4])

    def test_multiple_digits(self):
        self.assertEqual(increment_numerics([123, 456], 7), [123 + 7, 456 + 7])

    def test_mixed_list(self):
        self.assertEqual(increment_numerics(['a', 1, 'b', 2, 'c', 3], 5), ['a', 6, 'b', 7, 'c', 8])

    def test_negative_numbers(self):
        self.assertEqual(increment_numerics([-1, -2, -3], 5), [2, 0, -2])

    def test_large_numbers(self):
        self.assertEqual(increment_numerics([999999999, 888888888], 1), [1000000000, 888888889])

    def test_non_integer_input(self):
        self.assertEqual(increment_numerics(['a', 1, 'b', 2, 'c', 3.0], 5), ['a', 6, 'b', 7, 'c', 8.0])
