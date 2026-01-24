import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_all_positive(self):
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_all_negative(self):
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([-1, 2, -3, 4, -5]), 3)

    def test_zero_in_list(self):
        self.assertEqual(neg_count([0, -1, 2, -3, 4]), 1)

    def test_large_list(self):
        self.assertEqual(neg_count(list(range(-1000, 1000, 2))), 500)
