import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(index_minimum([[1, 2], [3, 4], [5, 1]]), 5)

    def test_edge_case_empty_input(self):
        with self.assertRaises(IndexError):
            index_minimum([])

    def test_edge_case_single_element_input(self):
        self.assertEqual(index_minimum([[1, 2]]), 1)

    def test_edge_case_multiple_minima_input(self):
        self.assertEqual(index_minimum([[1, 2], [3, 4], [5, 1]]), 5)

    def test_edge_case_max_value_input(self):
        self.assertEqual(index_minimum([[10, 2], [3, 4], [5, 1]]), 10)

    def test_edge_case_min_value_input(self):
        self.assertEqual(index_minimum([[1, 2], [3, 4], [5, 1]]), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            index_minimum("Invalid input")
