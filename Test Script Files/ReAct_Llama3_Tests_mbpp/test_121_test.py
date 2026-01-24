import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case1(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case2(self):
        A = [1, 2, 3, 4, 5]
        n = 0
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case3(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = -1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case4(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 0
        count = 3
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case5(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 0
        count = 2
        self.assertFalse(check_triplet(A, n, sum, count))
