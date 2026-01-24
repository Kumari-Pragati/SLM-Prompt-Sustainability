import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 9), (1, 2, 6))
        self.assertEqual(find_triplet_array([-1, 0, 2, 3, -4], 5, -1), (-1, 0, 3))

    def test_edge_cases(self):
        self.assertIsNone(find_triplet_array([1, 2, 3], 3, 4))
        self.assertIsNone(find_triplet_array([1, 2, 3], 3, 0))
        self.assertIsNone(find_triplet_array([], 0, 1))
        self.assertIsNone(find_triplet_array([1], 1, 2))
        self.assertIsNone(find_triplet_array([1, 2], 2, 3))

    def test_boundary_cases(self):
        self.assertIsNone(find_triplet_array([1, 2, 3], 3, 0))
        self.assertIsNone(find_triplet_array([1, 2, 3], 3, 4))
        self.assertIsNone(find_triplet_array([1, 2, 3], 2, 6))
        self.assertIsNone(find_triplet_array([1, 2, 3], 4, 2))

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_triplet_array, [1, 2, 3], 'a', 4)
        self.assertRaises(TypeError, find_triplet_array, [1, 2, 3], 4, 'a')
