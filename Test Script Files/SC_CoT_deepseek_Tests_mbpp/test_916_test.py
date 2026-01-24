import unittest

from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3))

    def test_edge_case(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 10
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3, 4))

    def test_invalid_input(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 'six'
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_no_triplet(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 15
        self.assertFalse(find_triplet_array(A, arr_size, sum))
