import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tn_gp(2, 3, 2), 12)
        self.assertEqual(tn_gp(3, 2, 2), 6)
        self.assertEqual(tn_gp(4, 4, 2), 32)

    def test_edge_and_boundary(self):
        self.assertEqual(tn_gp(0, 1, 1), 0)
        self.assertEqual(tn_gp(1, 0, 1), 0)
        self.assertEqual(tn_gp(1, 1, 0), TraceError)
        self.assertEqual(tn_gp(1, 1, 1), 1)
        self.assertEqual(tn_gp(-1, 1, 1), -1)
        self.assertEqual(tn_gp(1, 1, -1), -1)

    def test_complex(self):
        self.assertEqual(tn_gp(2, 10, 2), 200)
        self.assertEqual(tn_gp(3, 20, 2), 144000)
        self.assertEqual(tn_gp(4, 30, 2), 3603600)
        self.assertEqual(tn_gp(5, 40, 2), 180180160)
