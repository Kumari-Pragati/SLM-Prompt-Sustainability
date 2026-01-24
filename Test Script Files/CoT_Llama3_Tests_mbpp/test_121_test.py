import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):
    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 0
        count = 0
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case_sum_zero(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 0
        count = 3
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case_count_three(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = 0
        count = 3
        self.assertTrue(check_triplet(A, n, sum, count))

    def test_edge_case_n_zero(self):
        A = [1, 2, 3, 4, 5]
        n = 0
        sum = 0
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_edge_case_sum_negative(self):
        A = [1, 2, 3, 4, 5]
        n = 5
        sum = -1
        count = 0
        self.assertFalse(check_triplet(A, n, sum, count))

    def test_invalid_input_type(self):
        A = [1, 2, 3, 4, 5]
        n = 'five'
        sum = 0
        count = 0
        with self.assertRaises(TypeError):
            check_triplet(A, n, sum, count)

    def test_invalid_input_value(self):
        A = [1, 2, 3, 4, 5]
        n = 10
        sum = 0
        count = 0
        with self.assertRaises(IndexError):
            check_triplet(A, n, sum, count)
