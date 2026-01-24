import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3))

    def test_no_triplet(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 10
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_negative_numbers(self):
        A = [-1, -2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 5
        self.assertEqual(find_triplet_array(A, arr_size, sum), (-1, -2, 3))

    def test_duplicate_numbers(self):
        A = [1, 2, 2, 4, 5, 6]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 2))

    def test_empty_array(self):
        A = []
        arr_size = 0
        sum = 0
        self.assertFalse(find_triplet_array(A, arr_size, sum))
