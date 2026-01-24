import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(tn_ap(1, 2, 1), 4)
        self.assertEqual(tn_ap(5, 3, 2), 13)

    def test_edge_and_boundary(self):
        self.assertEqual(tn_ap(0, 1, 1), 1)
        self.assertEqual(tn_ap(100, 101, 1), 10001)
        self.assertEqual(tn_ap(0, 0, 1), 0)
        self.assertEqual(tn_ap(-1, 1, 1), -1)

    def test_negative_d(self):
        self.assertEqual(tn_ap(3, 4, -2), -9)

    def test_zero_d(self):
        self.assertEqual(tn_ap(3, 4, 0), 3)
