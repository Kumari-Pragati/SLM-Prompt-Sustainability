import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_find_triplet_array_found(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr_size = len(A)
        sum = 10
        self.assertTrue(find_triplet_array(A, arr_size, sum))
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 7))

    def test_find_triplet_array_not_found(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr_size = len(A)
        sum = 15
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_find_triplet_array_found_multiple(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr_size = len(A)
        sum = 12
        self.assertTrue(find_triplet_array(A, arr_size, sum))
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 3, 8))

    def test_find_triplet_array_empty_array(self):
        A = []
        arr_size = len(A)
        sum = 10
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_find_triplet_array_single_element_array(self):
        A = [1]
        arr_size = len(A)
        sum = 2
        self.assertFalse(find_triplet_array(A, arr_size, sum))
