import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(neg_count([1, 2, -3, 4, -5]), 2)
        self.assertEqual(neg_count([0, -1, 0, -2]), 3)
        self.assertEqual(neg_count([-5, -4, -3, -2, -1]), 5)

    def test_edge_case(self):
        self.assertEqual(neg_count([]), 0)
        self.assertEqual(neg_count([1]), 0)
        self.assertEqual(neg_count([-1]), 1)

    def test_boundary_case(self):
        self.assertEqual(neg_count([-0]), 1)
        self.assertEqual(neg_count([0.0]), 0)
