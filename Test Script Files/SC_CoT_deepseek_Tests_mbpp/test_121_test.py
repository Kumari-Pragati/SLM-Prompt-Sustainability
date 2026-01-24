import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_case(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case_small_sum(self):
        A = [1, 2, 3]
        n = len(A)
        sum = -1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case_large_sum(self):
        A = [1, 2, 3]
        n = len(A)
        sum = 6
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case_small_count(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = 2
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case_large_count(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = 4
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_invalid_input_negative_n(self):
        A = [1, -1, 0]
        n = -1
        sum = 0
        count = 0
        with self.assertRaises(Exception):
            check_triplet(A, n, sum, count)

    def test_invalid_input_negative_sum(self):
        A = [1, -1, 0]
        n = len(A)
        sum = -1
        count = 0
        with self.assertRaises(Exception):
            check_triplet(A, n, sum, count)

    def test_invalid_input_negative_count(self):
        A = [1, -1, 0]
        n = len(A)
        sum = 0
        count = -1
        with self.assertRaises(Exception):
            check_triplet(A, n, sum, count)
