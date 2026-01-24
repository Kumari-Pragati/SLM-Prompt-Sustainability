import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (2, 1), (3, 3)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_single_element(self):
        test_list = [(1, 2)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertRaises(ValueError, index_minimum, test_list)

    def test_edge_case_same_minimum_values(self):
        test_list = [(1, 2), (2, 2), (3, 3)]
        self.assertIn(index_minimum(test_list), [1, 2])

    def test_invalid_input_non_tuple(self):
        test_list = [(1, 2), (2, 1), '3', 3]
        self.assertRaises(TypeError, index_minimum, test_list)

    def test_invalid_input_non_integer_tuple_element(self):
        test_list = [(1, '2'), (2, 1), (3, 3)]
        self.assertRaises(TypeError, index_minimum, test_list)
