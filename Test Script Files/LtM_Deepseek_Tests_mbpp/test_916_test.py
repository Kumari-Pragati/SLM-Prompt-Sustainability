import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 6), (1, 2, 3))

    def test_edge_condition_empty_array(self):
        self.assertFalse(find_triplet_array([], 0, 6))

    def test_edge_condition_single_element(self):
        self.assertFalse(find_triplet_array([1], 1, 6))

    def test_edge_condition_two_elements(self):
        self.assertFalse(find_triplet_array([1, 2], 2, 6))

    def test_boundary_condition_min_max_values(self):
        self.assertFalse(find_triplet_array([-10000, -10000, -10000, 10000, 10000], 5, 0))

    def test_complex_case_no_triplet(self):
        self.assertFalse(find_triplet_array([1, 2, 3, 4, 5], 5, 10))

    def test_complex_case_with_duplicates(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5, 5], 6, 10), (2, 3, 5))
