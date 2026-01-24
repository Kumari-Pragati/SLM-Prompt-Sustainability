import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_simple_valid_input(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3))

    def test_edge_case_empty_input(self):
        A = []
        arr_size = len(A)
        sum = 0
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_edge_case_single_element_input(self):
        A = [1]
        arr_size = len(A)
        sum = 2
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_edge_case_two_element_input(self):
        A = [1, 2]
        arr_size = len(A)
        sum = 3
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_edge_case_max_sum_input(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 10
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 5))

    def test_edge_case_min_sum_input(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 1
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_edge_case_invalid_sum_input(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = -1
        self.assertFalse(find_triplet_array(A, arr_size, sum))
