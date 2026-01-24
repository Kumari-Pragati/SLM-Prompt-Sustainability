import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):
    def test_typical_case(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case(self):
        A = [1, 2, 3]
        n = len(A)
        sum = 6
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_boundary_case(self):
        A = [0, 0, 0]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_invalid_input(self):
        A = [1, 2, 3]
        n = -1
        sum = 0
        count = 0
        with self.assertRaises(IndexError):
            check_triplet(A, n, sum, count)
