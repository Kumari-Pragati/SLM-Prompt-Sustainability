import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 5), 2)

    def test_edge_condition_empty_array(self):
        self.assertEqual(first([], 3, 0), -1)

    def test_edge_condition_single_element(self):
        self.assertEqual(first([5], 5, 1), 0)
        self.assertEqual(first([5], 6, 1), -1)

    def test_edge_condition_all_elements_same(self):
        self.assertEqual(first([3, 3, 3, 3, 3], 3, 5), 0)

    def test_edge_condition_minimum_maximum_values(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 5), 0)
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 5), 4)

    def test_complex_input(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 4, 5), 3)
        self.assertEqual(first([1, 2, 3, 4, 5], 6, 5), -1)
