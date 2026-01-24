import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])

    def test_edge_condition_empty_input(self):
        self.assertEqual(specified_element([], 0), [])

    def test_edge_condition_N_equals_0(self):
        self.assertEqual(specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [1, 4, 7])

    def test_edge_condition_N_equals_last_index(self):
        self.assertEqual(specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [3, 6, 9])

    def test_boundary_condition_N_greater_than_last_index(self):
        with self.assertRaises(IndexError):
            specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)

    def test_boundary_condition_N_less_than_0(self):
        with self.assertRaises(IndexError):
            specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1)
