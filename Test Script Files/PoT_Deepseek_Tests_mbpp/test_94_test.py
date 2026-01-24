import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(index_minimum([(1, 2), (2, 1), (3, 0)]), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(index_minimum([(1, 1)]), 1)

    def test_boundary_case_same_minimum(self):
        self.assertEqual(index_minimum([(1, 2), (2, 2), (3, 2)]), 1)

    def test_corner_case_empty_list(self):
        with self.assertRaises(ValueError):
            index_minimum([])

    def test_corner_case_negative_values(self):
        self.assertEqual(index_minimum([(1, -2), (2, -1), (3, 0)]), 3)
