import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(return_sum({1: 2, 3: 4, 5: 6}), 15)

    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_element_dict(self):
        self.assertEqual(return_sum({1: 10}), 10)

    def test_negative_numbers(self):
        self.assertEqual(return_sum({1: -2, 3: -4, 5: -6}), -15)

    def test_float_numbers(self):
        self.assertAlmostEqual(return_sum({1: 2.5, 3: 4.5, 5: 6.5}), 13.5)

    def test_non_integer_keys(self):
        with self.assertRaises(TypeError):
            return_sum({"a": 1, "b": 2, "c": 3})

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            return_sum({1: "two", 3: "four", 5: "six"})
