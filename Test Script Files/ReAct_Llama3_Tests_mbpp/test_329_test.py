import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_single_positive(self):
        self.assertEqual(neg_count([1]), 0)

    def test_single_negative(self):
        self.assertEqual(neg_count([-1]), 1)

    def test_multiple_positive(self):
        self.assertEqual(neg_count([1, 2, 3]), 0)

    def test_multiple_negative(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)

    def test_mixed_list(self):
        self.assertEqual(neg_count([1, -2, 3, -4]), 2)

    def test_list_with_zero(self):
        self.assertEqual(neg_count([0, 1, -2, 3]), 1)
