import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(find_triplet_array([], 0, 3))

    def test_single_element(self):
        self.assertFalse(find_triplet_array([1], 1, 3))

    def test_two_elements(self):
        self.assertFalse(find_triplet_array([1, 2], 2, 3))

    def test_three_elements_no_triplet(self):
        self.assertFalse(find_triplet_array([1, 2, 3], 3, 4))

    def test_three_elements_triplet(self):
        self.assertEqual(find_triplet_array([1, 2, 4], 3, 7), (1, 2, 4))

    def test_four_elements_triplet(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 6], 4, 7), (1, 2, 4))

    def test_five_elements_triplet(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 9), (1, 2, 6))
