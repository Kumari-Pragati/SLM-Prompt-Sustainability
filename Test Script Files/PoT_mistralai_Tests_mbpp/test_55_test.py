import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tn_gp(2, 3, 2), 16)
        self.assertEqual(tn_gp(5, 4, 3), 60)

    def test_edge_cases(self):
        self.assertEqual(tn_gp(0, 1, 1), 0)
        self.assertEqual(tn_gp(1, 0, 1), 0)
        self.assertEqual(tn_gp(1, 1, 0), 0)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, tn_gp, -1, 2, 3)
        self.assertRaises(ValueError, tn_gp, 1, -2, 3)
        self.assertRaises(ValueError, tn_gp, 1, 2, -3)
