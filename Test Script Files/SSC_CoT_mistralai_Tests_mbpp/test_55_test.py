import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(tn_gp(2, 3, 2), 16)
        self.assertEqual(tn_gp(-5, 4, 3), -60)

    def test_edge_input(self):
        self.assertEqual(tn_gp(0, 1, 1), 0)
        self.assertEqual(tn_gp(1, 0, 1), 0)
        self.assertEqual(tn_gp(1, 1, 0), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            tn_gp(-1, 3, 2)
        with self.assertRaises(ValueError):
            tn_gp(1, -3, 2)
        with self.assertRaises(ValueError):
            tn_gp(1, 3, -2)
