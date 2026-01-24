import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(return_sum({'a': 1}), 1)

    def test_multiple_values_dict(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_dict_with_negative_values(self):
        self.assertEqual(return_sum({'a': 1, 'b': -2, 'c': 3}), 2)

    def test_dict_with_zero_values(self):
        self.assertEqual(return_sum({'a': 0, 'b': 0, 'c': 0}), 0)

    def test_dict_with_non_integer_values(self):
        self.assertEqual(return_sum({'a': 1.5, 'b': -2.5, 'c': 3.5}), 2.5)

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            return_sum('not a dict')
