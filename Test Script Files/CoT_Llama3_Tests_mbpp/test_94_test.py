import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 5), (2, 3), (3, 8), (4, 2)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_empty_list(self):
        test_list = []
        with self.assertRaises(IndexError):
            index_minimum(test_list)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 5)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_multiple_minima(self):
        test_list = [(1, 5), (2, 3), (3, 3)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            index_minimum("Invalid input")

    def test_invalid_input_non_tuple(self):
        test_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            index_minimum(test_list)
