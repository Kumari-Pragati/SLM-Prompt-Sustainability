import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_true_case(self):
        A = [1, 2, -2]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_false_case1(self):
        A = [1, 2, -2]
        n = len(A)
        sum = 1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_false_case2(self):
        A = [1, 2, -2]
        n = len(A)
        sum = 0
        count = 2
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_false_case3(self):
        A = [1, 2, -2]
        n = len(A)
        sum = -1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_false_case4(self):
        A = [1, 2, -2]
        n = len(A)
        sum = 0
        count = 3
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case1(self):
        A = [1]
        n = len(A)
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case2(self):
        A = [1, 2]
        n = len(A)
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))
