import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4], 4, 7), (1, 2, 4))

    def test_sum_greater_than_array_sum(self):
        self.assertFalse(find_triplet_array([1, 2, 3], 3, 10))

    def test_sum_less_than_array_minimum(self):
        self.assertFalse(find_triplet_array([1, 2, 3], 3, -1))

    def test_single_element_array(self):
        self.assertFalse(find_triplet_array([1], 1, 2))

    def test_two_elements_array(self):
        self.assertFalse(find_triplet_array([1, 2], 2, 3))

    def test_duplicate_elements(self):
        self.assertEqual(find_triplet_array([1, 1, 2, 3], 4, 4), (1, 1, 2))

    def test_multiple_solutions(self):
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5, 6], 6, 10), (1, 2, 7))
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5, 6], 6, 10), (1, 4, 5))
