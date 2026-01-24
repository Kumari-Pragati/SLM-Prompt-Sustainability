import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_edge_cases(self):
        self.assertEqual(return_sum({}), 0)
        self.assertEqual(return_sum({'a': 5}), 5)

    def test_negative_numbers(self):
        self.assertEqual(return_sum({'a': -1, 'b': 2, 'c': -3}), -2)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            return_sum({'a': 'hello', 'b': 2, 'c': 3})

    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_dict_with_single_element(self):
        self.assertEqual(return_sum({'a': 5}), 5)

    def test_dict_with_multiple_elements(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3, 'd': 4}), 10)
