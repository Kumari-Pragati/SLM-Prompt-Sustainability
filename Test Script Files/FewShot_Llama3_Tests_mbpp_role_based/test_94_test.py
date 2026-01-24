import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 3), (2, 1), (3, 2), (4, 4)]
        self.assertEqual(index_minimum(test_list), 2)

    def test_edge_case_empty_list(self):
        test_list = []
        with self.assertRaises(IndexError):
            index_minimum(test_list)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 3)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_multiple_minima(self):
        test_list = [(1, 3), (2, 1), (3, 2), (4, 1)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            index_minimum("not a list")
