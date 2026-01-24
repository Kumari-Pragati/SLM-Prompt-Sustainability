import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, -1, -2, -3]
        self.assertTrue(check_triplet(A, len(A), 0, 0))

    def test_no_triplet(self):
        A = [1, 2, 3, 4, 5]
        self.assertFalse(check_triplet(A, len(A), 6, 0))

    def test_negative_sum(self):
        A = [1, 2, 3, -1, -2, -3]
        self.assertFalse(check_triplet(A, len(A), -1, 0))

    def test_empty_array(self):
        A = []
        self.assertFalse(check_triplet(A, len(A), 0, 0))

    def test_single_element(self):
        A = [0]
        self.assertFalse(check_triplet(A, len(A), 0, 0))

    def test_large_array(self):
        A = list(range(-100, 100, 2))  # Even numbers from -98 to 98
        self.assertTrue(check_triplet(A, len(A), 0, 0))

    def test_large_negative_sum(self):
        A = list(range(-100, 100, 2))  # Even numbers from -98 to 98
        self.assertFalse(check_triplet(A, len(A), -200, 0))
