import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(index_minimum([[1, 2], [3, 4], [5, 1]]), 5)

    def test_edge_case_minimal(self):
        self.assertEqual(index_minimum([[1, 2], [3, 4]]), 1)

    def test_edge_case_maximal(self):
        self.assertEqual(index_minimum([[5, 1], [3, 4]]), 5)

    def test_edge_case_single_element(self):
        self.assertEqual(index_minimum([[1, 2]]), 1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(ValueError):
        index_minimum([])

    def test_edge_case_single_element_minimal(self):
        self.assertEqual(index_minimum([[1, 2]]), 1)

    def test_edge_case_single_element_maximal(self):
        self.assertEqual(index_minimum([[5, 1]]), 5)
