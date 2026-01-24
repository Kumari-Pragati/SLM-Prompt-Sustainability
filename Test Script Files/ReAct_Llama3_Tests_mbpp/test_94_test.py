import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_typical_case(self):
        test_list = [(1, 2), (3, 1), (4, 3), (5, 4)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_empty_list(self):
        test_list = []
        with self.assertRaises(IndexError):
            index_minimum(test_list)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 2)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_multiple_minima(self):
        test_list = [(1, 2), (2, 1), (3, 3)]
        self.assertEqual(index_minimum(test_list), 1)

    def test_edge_case_negative_numbers(self):
        test_list = [(-1, 2), (-3, 1), (-4, 3), (-5, 4)]
        self.assertEqual(index_minimum(test_list), -5)

    def test_edge_case_non_numeric_values(self):
        test_list = [('a', 2), ('b', 1), ('c', 3), ('d', 4)]
        self.assertEqual(index_minimum(test_list), 'a')
