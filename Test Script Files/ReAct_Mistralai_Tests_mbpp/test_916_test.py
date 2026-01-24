import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_find_triplet_array_positive(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 9), (1, 2, 6))
        self.assertEqual(find_triplet_array([-1, 0, 2, 3, -4], 5, -1), (-1, 0, 3) )
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 15), None)

    def test_find_triplet_array_empty_list(self):
        self.assertIsNone(find_triplet_array([], 0, 1))

    def test_find_triplet_array_single_element(self):
        self.assertIsNone(find_triplet_array([1], 1, 2))

    def test_find_triplet_array_negative_sum(self):
        self.assertIsNone(find_triplet_array([1, 2, 3], 3, -1))

    def test_find_triplet_array_duplicate_elements(self):
        self.assertEqual(find_triplet_array([1, 1, 1, 2, 3], 5, 4), (1, 1, 2))

    def test_find_triplet_array_large_sum(self):
        self.assertIsNone(find_triplet_array([1, 2, 3, 4, 5], 5, 20))
