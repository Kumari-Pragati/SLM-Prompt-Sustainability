import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_edge_cases(self):
        self.assertEqual(neg_count([]), 0)
        self.assertEqual(neg_count([0]), 0)

    def test_corner_cases(self):
        self.assertEqual(neg_count([-1]), 1)
        self.assertEqual(neg_count([0, -1]), 1)
        self.assertEqual(neg_count([0, 1]), 0)
