import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 9), (1, 2, 6))
        self.assertEqual(find_triplet_array([-1, 0, 2, 3, -4], 5, -1), (-1, 0, 3))
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 15), False)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_triplet_array([], 0, 1))

    def test_edge_case_single_element(self):
        self.assertIsNone(find_triplet_array([1], 1, 2))

    def test_edge_case_two_elements(self):
        self.assertIsNone(find_triplet_array([1, 2], 2, 3))

    def test_corner_case_negative_sum(self):
        self.assertIsNone(find_triplet_array([1, 2, 3], 3, -1))
