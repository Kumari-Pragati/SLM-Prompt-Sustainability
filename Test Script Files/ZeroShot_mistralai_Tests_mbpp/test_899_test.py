import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_check_positive_sequence(self):
        self.assertTrue(check([1, 2, 3, 4, 5], len(check([1, 2, 3, 4, 5]))))

    def test_check_negative_sequence(self):
        self.assertTrue(check([-1, -2, -3, -4, -5], len(check([-1, -2, -3, -4, -5]))))

    def test_check_mixed_sequence(self):
        self.assertTrue(check([1, -2, 3, -4, 5], len(check([1, -2, 3, -4, 5]))))

    def test_check_single_element(self):
        self.assertTrue(check([1], len(check([1]))))

    def test_check_empty_list(self):
        self.assertFalse(check([], len(check([]))))

    def test_check_decreasing_sequence(self):
        self.assertFalse(check([5, 4, 3, 2, 1], len(check([5, 4, 3, 2, 1]))))

    def test_check_increasing_sequence_with_zero(self):
        self.assertTrue(check([0, 1, 2, 3, 4], len(check([0, 1, 2, 3, 4]))))
