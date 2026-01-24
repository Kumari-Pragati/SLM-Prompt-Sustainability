import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(neg_count([]), 0)
        self.assertEqual(neg_count([1, 2, 3]), 0)

    def test_zero_list(self):
        self.assertEqual(neg_count([0]), 1)
        self.assertEqual(neg_count([0, 0]), 1)

    def test_negative_list(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)
        self.assertEqual(neg_count([-1, 0, -3]), 2)

    def test_mixed_list(self):
        self.assertEqual(neg_count([-1, 0, 1, -2, 3]), 2)
        self.assertEqual(neg_count([-1, 0, 1, 0, -2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_none_list(self):
        self.assertRaises(TypeError, neg_count, None)
