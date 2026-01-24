import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(tn_ap(10, 5, 2), 22)
        self.assertEqual(tn_ap(-10, 5, 2), -17)
        self.assertEqual(tn_ap(0, 0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(tn_ap(0, 0, 1), 0)
        self.assertEqual(tn_ap(1, 0, 1), 1)
        self.assertEqual(tn_ap(1, 1, 0), 1)

    def test_negative_d(self):
        self.assertEqual(tn_ap(10, 5, -2), -18)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, tn_ap, "a", 5, 2)
        self.assertRaises(TypeError, tn_ap, 10, "n", 2)
        self.assertRaises(TypeError, tn_ap, 10, 5, "d")
