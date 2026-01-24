import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3))

    def test_edge_case_with_single_element(self):
        A = [1]
        arr_size = len(A)
        sum = 1
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_edge_case_with_two_elements(self):
        A = [1, 2]
        arr_size = len(A)
        sum = 3
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_boundary_case_with_empty_array(self):
        A = []
        arr_size = len(A)
        sum = 1
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_corner_case_with_duplicate_elements(self):
        A = [1, 1, 1, 1]
        arr_size = len(A)
        sum = 3
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 1, 1))

    def test_corner_case_with_large_array(self):
        A = list(range(1, 1001))
        arr_size = len(A)
        sum = 1002
        self.assertFalse(find_triplet_array(A, arr_size, sum))
