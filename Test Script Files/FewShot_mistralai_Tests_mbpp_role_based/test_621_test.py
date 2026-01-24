import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(increment_numerics([1, 'a', 3, 'b', 5], 2), ['3', 'a', '5', 'b', '7'])

    def test_empty_list(self):
        self.assertEqual(increment_numerics([], 3), [])

    def test_single_digit(self):
        self.assertEqual(increment_numerics([1], 2), [3])

    def test_multiple_digits(self):
        self.assertEqual(increment_numerics([123, 456], 7), [123 + 7, 456 + 7])

    def test_negative_numbers(self):
        self.assertEqual(increment_numerics([-1, -2], 3), [-1 + 3, -2 + 3])

    def test_non_integer_input(self):
        self.assertEqual(increment_numerics(['a', 'b'], 2), ['a', 'b'])
