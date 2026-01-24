import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_case(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case_no_elements(self):
        A = []
        n = len(A)
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case_sum_not_zero(self):
        A = [1, -1, 2]
        n = len(A)
        sum = 1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_boundary_case_negative_elements(self):
        A = [-1, -1, -1]
        n = len(A)
        sum = -1
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_corner_case_large_array(self):
        A = list(range(-1000, 1000, 1))
        n = len(A)
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))
