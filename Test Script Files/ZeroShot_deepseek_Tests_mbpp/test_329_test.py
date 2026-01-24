import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_negative_numbers(self):
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([-1, 2, -3, 4, -5]), 3)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_single_negative_number(self):
        self.assertEqual(neg_count([-1]), 1)

    def test_single_positive_number(self):
        self.assertEqual(neg_count([1]), 0)

    def test_zero(self):
        self.assertEqual(neg_count([0]), 0)
