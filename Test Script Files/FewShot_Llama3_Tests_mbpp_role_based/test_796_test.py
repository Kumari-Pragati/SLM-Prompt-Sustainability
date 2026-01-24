import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(return_sum({'a': 5}), 5)

    def test_multiple_values_dict(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_dict_with_negative_values(self):
        self.assertEqual(return_sum({'a': -1, 'b': 2, 'c': -3}), -2)

    def test_dict_with_float_values(self):
        self.assertEqual(return_sum({'a': 1.5, 'b': 2.5, 'c': 3.5}), 7.5)
