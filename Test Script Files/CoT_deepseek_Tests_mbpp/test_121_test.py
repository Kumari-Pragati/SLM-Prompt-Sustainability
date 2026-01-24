import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        n = len(A)
        sum = 6
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_no_triplet(self):
        A = [1, 2, 3, 4, 5]
        n = len(A)
        sum = 10
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_negative_sum(self):
        A = [1, 2, 3, 4, 5]
        n = len(A)
        sum = -1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_count_not_3(self):
        A = [1, 2, 3, 4, 5]
        n = len(A)
        sum = 6
        count = 2
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_empty_array(self):
        A = []
        n = 0
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))
