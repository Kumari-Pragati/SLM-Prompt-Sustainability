import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(return_sum({1: 1, 2: 2, 3: 3}), 6)

    def test_single_value(self):
        self.assertEqual(return_sum({1: 10}), 10)

    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_negative_values(self):
        self.assertEqual(return_sum({1: -1, 2: -2, 3: -3}), -6)

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            return_sum({1: 1.5, 2: 2.5, 3: 3.5})

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            return_sum({"a": "apple", "b": "banana"})

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            return_sum("not a dictionary")
