import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), ((6, 8), (10, 12)))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ())

    def test_boundary_case_single_tuple(self):
        self.assertEqual(add_nested_tuples(((1, 2)), ((3, 4))), ((4, 6)))

    def test_corner_case_different_length_tuples(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4, 5)), ((6, 7), (8, 9))), ((7, 9), (11, 13)))

    def test_invalid_input_mismatched_length_tuples(self):
        with self.assertRaises(ValueError):
            add_nested_tuples(((1, 2), (3, 4)), ((5, 6)))
