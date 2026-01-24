import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(find_triplet_array([], 0, 0))

    def test_single_element(self):
        for element in [0, 1, -1]:
            self.assertFalse(find_triplet_array([element], 1, 0))

    def test_two_elements_sum_to_zero(self):
        self.assertTrue(find_triplet_array([1, -1], 2, 0))

    def test_two_elements_sum_to_non_zero(self):
        self.assertFalse(find_triplet_array([1, 2], 2, 3))

    def test_three_elements_sum_to_zero(self):
        self.assertTrue(find_triplet_array([1, 1, -2], 3, 0))

    def test_three_elements_sum_to_non_zero(self):
        self.assertFalse(find_triplet_array([1, 1, 1], 3, 2))

    def test_negative_numbers(self):
        self.assertTrue(find_triplet_array([-1, 0, 1], 3, 0))

    def test_large_numbers(self):
        self.assertTrue(find_triplet_array([100, 200, 300], 3, 600))

    def test_invalid_input_arr_size_zero(self):
        with self.assertRaises(IndexError):
            find_triplet_array([1, 2, 3], 0, 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            find_triplet_array([1, 2, 3], 3, 0)
