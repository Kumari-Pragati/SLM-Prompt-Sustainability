import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(return_sum({'a': 5}), 5)

    def test_multiple_values_dict(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_negative_values_dict(self):
        self.assertEqual(return_sum({'a': -1, 'b': -2, 'c': -3}), -6)

    def test_dict_with_zero(self):
        self.assertEqual(return_sum({'a': 0, 'b': 0, 'c': 0}), 0)

    def test_dict_with_negative_and_positive(self):
        self.assertEqual(return_sum({'a': -1, 'b': 2, 'c': 3}), 4)
