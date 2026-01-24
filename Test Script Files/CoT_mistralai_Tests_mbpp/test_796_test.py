import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_value(self):
        self.assertEqual(return_sum({1: 1}), 1)

    def test_multiple_values(self):
        self.assertEqual(return_sum({1: 1, 2: 2, 3: 3}), 6)

    def test_negative_values(self):
        self.assertEqual(return_sum({1: -1, 2: -2, 3: -3}), -6)

    def test_mixed_values(self):
        self.assertEqual(return_sum({1: 1, 2: -2, 3: 3}), 2)

    def test_key_error(self):
        with self.assertRaises(KeyError):
            return_sum({1: 1, 2: 2})

    def test_non_numeric_value(self):
        with self.assertRaises(TypeError):
            return_sum({1: 'string'})
