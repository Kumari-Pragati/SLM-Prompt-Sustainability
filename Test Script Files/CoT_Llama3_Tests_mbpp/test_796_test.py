import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_return_sum_with_valid_input(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_return_sum_with_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_return_sum_with_single_value_dict(self):
        self.assertEqual(return_sum({'a': 5}), 5)

    def test_return_sum_with_negative_values(self):
        self.assertEqual(return_sum({'a': -1, 'b': 2, 'c': -3}), -2)

    def test_return_sum_with_non_integer_values(self):
        self.assertEqual(return_sum({'a': 1.5, 'b': 2.5, 'c': 3.5}), 7.0)

    def test_return_sum_with_mixed_types(self):
        self.assertEqual(return_sum({'a': 1, 'b': 'hello', 'c': 3.5}), 4.5)
