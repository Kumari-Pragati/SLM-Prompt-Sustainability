import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), (((6, 8),),))

    def test_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ((),))

    def test_single_tuple(self):
        self.assertEqual(add_nested_tuples(((1, 2),)), ((),))

    def test_mismatched_tuples(self):
        with self.assertRaises(ValueError):
            add_nested_tuples(((1, 2), (3, 4)), (1, 2))
