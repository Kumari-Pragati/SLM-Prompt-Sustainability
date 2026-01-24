import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(return_sum({1: 2, 3: 4}), 7)

    def test_empty_input(self):
        self.assertEqual(return_sum({}), 0)

    def test_negative_numbers(self):
        self.assertEqual(return_sum({1: -2, 3: -4}), -7)

    def test_large_numbers(self):
        self.assertEqual(return_sum({1: 1000000, 2: 2000000}), 3000000)

    def test_float_numbers(self):
        self.assertAlmostEqual(return_sum({1: 1.5, 2: 2.5}), 4.0)

    def test_mixed_numbers(self):
        self.assertEqual(return_sum({1: 2, 3: -4, 5: 6}), 4)
