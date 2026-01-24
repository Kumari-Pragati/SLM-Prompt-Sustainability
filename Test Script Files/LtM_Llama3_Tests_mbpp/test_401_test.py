import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((4, 6),))

    def test_empty_inputs(self):
        self.assertEqual(add_nested_tuples((), ()), ())
        self.assertEqual(add_nested_tuples((1, 2), ()), ((1, 2),))

    def test_single_tuple(self):
        self.assertEqual(add_nested_tuples((1, 2, 3), ()), ((1, 2, 3),))

    def test_zero_length_tuples(self):
        self.assertEqual(add_nested_tuples((), (1, 2)), ())
        self.assertEqual(add_nested_tuples((1, 2), ()), ((1, 2),))

    def test_non_integer_values(self):
        self.assertEqual(add_nested_tuples((1, 2.5), (3, 4)), ((4, 6.5),))

    def test_negative_values(self):
        self.assertEqual(add_nested_tuples((-1, 2), (-3, 4)), ((-2, 6),))

    def test_mixed_sign_values(self):
        self.assertEqual(add_nested_tuples((-1, 2), (3, -4)), ((2, -2),))
