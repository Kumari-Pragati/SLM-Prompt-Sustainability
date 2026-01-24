import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):
    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 10
        self.assertEqual(find_triplet_array(A, arr_size, sum), (3, 4, 3))

    def test_edge_case(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 0
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, -1, -1))

    def test_boundary_case(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 1000
        self.assertEqual(find_triplet_array(A, arr_size, sum), False)

    def test_invalid_input(self):
        A = [1, 2, 3, 4, 5, 6]
        arr_size = len(A)
        sum = 'ten'
        with self.assertRaises(TypeError):
            find_triplet_array(A, arr_size, sum)
