import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(index_minimum([(1, 2), (2, 1), (3, 3)]), 1)

    def test_edge_condition_empty_list(self):
        self.assertIsNone(index_minimum([]))

    def test_boundary_condition_minimum_value(self):
        self.assertEqual(index_minimum([(1, 1), (2, 2), (3, 3)]), 1)

    def test_boundary_condition_maximum_value(self):
        self.assertEqual(index_minimum([(1, 3), (2, 2), (3, 1)]), 3)

    def test_complex_input(self):
        self.assertEqual(index_minimum([(1, 2), (2, 1), (3, 2)]), 2)
