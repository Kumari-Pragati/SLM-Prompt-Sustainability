import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):
    def test_found_triplet(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 9
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 6))

    def test_not_found_triplet(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 10
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_single_element_array(self):
        A = [1]
        arr_size = len(A)
        sum = 2
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_empty_array(self):
        A = []
        arr_size = len(A)
        sum = 2
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_invalid_sum(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = -1
        self.assertFalse(find_triplet_array(A, arr_size, sum))
