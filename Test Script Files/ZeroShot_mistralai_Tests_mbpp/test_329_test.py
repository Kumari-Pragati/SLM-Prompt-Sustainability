import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_positive_list(self):
        self.assertEqual(neg_count([1, 2, 3, 4]), 0)

    def test_negative_list(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)

    def test_mixed_list(self):
        self.assertEqual(neg_count([-1, 0, 1, -2]), 2)
