import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(return_sum({1: 2, 2: 3, 3: 4}), 9)

    def test_negative_numbers(self):
        self.assertEqual(return_sum({1: -2, 2: -3, 3: -4}), -9)

    def test_mixed_numbers(self):
        self.assertEqual(return_sum({1: -2, 2: 3, 3: -4, 4: 5}), 4)

    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_value(self):
        self.assertEqual(return_sum({1: 10}), 10)
