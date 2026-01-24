import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_triplet([], len([]), 0, 0))

    def test_single_element(self):
        for n in range(1, 100):
            self.assertFalse(check_triplet([n], n, 0, 0))

    def test_two_elements_sum_zero(self):
        self.assertTrue(check_triplet([1, -1], 1, 0, 0))
        self.assertFalse(check_triplet([1, 2], 1, 0, 0))

    def test_two_elements_sum_non_zero(self):
        for a in range(1, 100):
            for b in range(1, 100):
                if a + b == 0:
                    self.assertTrue(check_triplet([a, b], 1, 0, 0))
                else:
                    self.assertFalse(check_triplet([a, b], 1, a + b, 0))

    def test_three_elements_sum_zero(self):
        for a in range(1, 100):
            for b in range(1, a):
                for c in range(1, a - b + 1):
                    self.assertTrue(check_triplet([a, b, a - b - c], 2, 0, 0))

    def test_three_elements_sum_non_zero(self):
        for a in range(1, 100):
            for b in range(1, a):
                for c in range(1, a - b + 1):
                    if a + b + c == 0:
                        self.assertFalse(check_triplet([a, b, a - b - c], 2, 0, 0))
                    else:
                        self.assertFalse(check_triplet([a, b, a - b - c], 2, a + b + c, 0))

    def test_invalid_count(self):
        self.assertRaises(ValueError, check_triplet, [1, 2, 3], 4, 0, 0)
        self.assertRaises(ValueError, check_triplet, [], 3, 0, 0)
