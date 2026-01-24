import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(neg_count([1, 2, -3, 4, -5]), 2)
        self.assertEqual(neg_count([-1, 0, -2, 3, -4]), 4)
        self.assertEqual(neg_count([-5, -4, -3, -2, -1]), 5)

    def test_edge_input(self):
        self.assertEqual(neg_count([0]), 1)
        self.assertEqual(neg_count([-0]), 1)
        self.assertEqual(neg_count([-1e10]), 1)
        self.assertEqual(neg_count([1e10]), 0)

    def test_boundary_input(self):
        self.assertEqual(neg_count([-1, 0]), 1)
        self.assertEqual(neg_count([0, -1]), 1)
        self.assertEqual(neg_count([-1, 0, 1]), 1)
        self.assertEqual(neg_count([1, 0, -1]), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, neg_count, 123)
        self.assertRaises(TypeError, neg_count, (1, 2, -3))
