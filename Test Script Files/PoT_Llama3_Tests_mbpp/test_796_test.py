import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_edge_case_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_edge_case_single_value_dict(self):
        self.assertEqual(return_sum({'a': 5}), 5)

    def test_edge_case_dict_with_negative_values(self):
        self.assertEqual(return_sum({'a': 1, 'b': -2, 'c': 3}), 2)

    def test_edge_case_dict_with_zero_values(self):
        self.assertEqual(return_sum({'a': 0, 'b': 0, 'c': 0}), 0)

    def test_edge_case_dict_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            return_sum({'a': 'hello', 'b': 2, 'c': 3})

    def test_edge_case_dict_with_mixed_types(self):
        with self.assertRaises(TypeError):
            return_sum({'a': 1, 'b': 'hello', 'c': 3})
