import unittest

from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((1, 2), (3, 4))
        test_tup2 = ((5, 6), (7, 8))
        expected_output = ((6, 8), (10, 12))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), expected_output)

    def test_edge_case(self):
        test_tup1 = ((0, 0), (0, 0))
        test_tup2 = ((0, 0), (0, 0))
        expected_output = ((0, 0), (0, 0))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), expected_output)

    def test_boundary_case(self):
        test_tup1 = ((1000, 2000), (3000, 4000))
        test_tup2 = ((5000, 6000), (7000, 8000))
        expected_output = ((6000, 8000), (10000, 12000))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), expected_output)

    def test_invalid_input(self):
        test_tup1 = ((1, 2), (3, 4))
        test_tup2 = "not a tuple"
        with self.assertRaises(TypeError):
            add_nested_tuples(test_tup1, test_tup2)
