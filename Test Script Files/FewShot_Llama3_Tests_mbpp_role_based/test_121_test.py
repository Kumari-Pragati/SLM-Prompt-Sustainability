import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):
    def test_valid_triplet(self):
        A = [1, 2, 3]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_invalid_triplet(self):
        A = [1, 2, 3]
        n = len(A)
        sum = 1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_zero_sum(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_negative_sum(self):
        A = [1, -2, 3]
        n = len(A)
        sum = -1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_zero_count(self):
        A = [1, 2, 3]
        n = len(A)
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_large_n(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(A)
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))
