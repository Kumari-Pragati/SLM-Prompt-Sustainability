import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((1, 2), (3, 4))
        test_tup2 = ((5, 6), (7, 8))
        expected_output = ((6, 8), (10, 12))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), expected_output)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_output = ()
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), expected_output)

    def test_single_tuple(self):
        test_tup1 = (1, 2)
        test_tup2 = (3, 4)
        expected_output = (4, 6)
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), expected_output)

    def test_different_length_tuples(self):
        test_tup1 = ((1, 2), (3, 4, 5))
        test_tup2 = ((5, 6), (7, 8))
        with self.assertRaises(ValueError):
            add_nested_tuples(test_tup1, test_tup2)

    def test_non_tuple_input(self):
        test_tup1 = [1, 2]
        test_tup2 = (3, 4)
        with self.assertRaises(TypeError):
            add_nested_tuples(test_tup1, test_tup2)
