import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(return_sum({1: 1, 2: 2, 3: 3}), 6)

    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_element(self):
        self.assertEqual(return_sum({1: 10}), 10)

    def test_negative_numbers(self):
        self.assertEqual(return_sum({1: -1, 2: -2, 3: -3}), -6)

    def test_float_numbers(self):
        self.assertAlmostEqual(return_sum({1: 1.5, 2: 2.5, 3: 3.5}), 7.5)

    def test_large_numbers(self):
        self.assertEqual(return_sum({1: 1000000, 2: 2000000, 3: 3000000}), 6000000)
