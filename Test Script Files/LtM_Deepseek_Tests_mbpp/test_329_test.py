import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(neg_count([1, 2, 3]), 0)

    def test_simple_negative_numbers(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([1, -2, 3, -4]), 2)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_single_zero(self):
        self.assertEqual(neg_count([0]), 0)

    def test_single_negative_zero(self):
        self.assertEqual(neg_count([-0]), 1)

    def test_large_numbers(self):
        self.assertEqual(neg_count([-10**6, 10**6, -10**7]), 2)

    def test_float_numbers(self):
        self.assertEqual(neg_count([-1.5, 2.5, -3.5]), 2)

    def test_mixed_float_and_int(self):
        self.assertEqual(neg_count([1, -2.5, 3, -4]), 2)
