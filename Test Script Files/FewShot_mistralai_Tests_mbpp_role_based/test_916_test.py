import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):
    def test_triplet_found(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 9), (1, 4, 4))

    def test_triplet_not_found(self):
        self.assertIsNone(find_triplet_array([1, 2, 3, 4, 5], 5, 10))

    def test_empty_list(self):
        self.assertIsNone(find_triplet_array([], 0, 0))

    def test_single_element(self):
        self.assertIsNone(find_triplet_array([1], 1, 2))

    def test_two_elements(self):
        self.assertIsNone(find_triplet_array([1, 2], 2, 3))

    def test_negative_numbers(self):
        self.assertIsNone(find_triplet_array([-1, -2, -3], 3, 0))
