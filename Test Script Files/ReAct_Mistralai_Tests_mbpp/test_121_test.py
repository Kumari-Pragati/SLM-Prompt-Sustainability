import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_triplet([], 0, 0, 0))

    def test_single_element(self):
        for element in range(-100, 101):
            self.assertFalse(check_triplet([element], 1, element, 0))

    def test_two_elements_sum_zero(self):
        self.assertTrue(check_triplet([1, -1], 2, 0, 0))
        self.assertFalse(check_triplet([1, 2], 2, 0, 0))

    def test_two_elements_sum_non_zero(self):
        for a in range(-100, 101):
            for b in range(a + 1, 101):
                self.assertFalse(check_triplet([a, b], 2, a + b, 0))

    def test_three_elements_sum_zero(self):
        self.assertTrue(check_triplet([1, 1, -1], 3, 0, 0))
        self.assertFalse(check_triplet([1, 1, 1], 3, 0, 0))

    def test_three_elements_sum_non_zero(self):
        for a in range(-100, 101):
            for b in range(a + 1, 101):
                for c in range(b + 1, 101):
                    self.assertFalse(check_triplet([a, b, c], 3, a + b + c, 0))

    def test_count_exceeds_3(self):
        for _ in range(4, 101):
            self.assertFalse(check_triplet([1], _, 1, _))

    def test_negative_sum(self):
        self.assertFalse(check_triplet([1], 1, -1, 0))
