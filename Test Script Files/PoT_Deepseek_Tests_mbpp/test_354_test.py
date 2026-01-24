import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(tn_ap(5, 10, 2), 25)
        self.assertEqual(tn_ap(1, 5, 3), 14)

    def test_edge_cases(self):
        self.assertEqual(tn_ap(0, 0, 0), 0)
        self.assertEqual(tn_ap(100, 1, 0), 100)

    def test_boundary_cases(self):
        self.assertEqual(tn_ap(1000, 1000, 1), 2000000)
        self.assertEqual(tn_ap(1, 1000, 1), 999)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tn_ap("a", 10, 2)
        with self.assertRaises(TypeError):
            tn_ap(10, "b", 2)
        with self.assertRaises(TypeError):
            tn_ap(10, 10, "c")
        with self.assertRaises(ValueError):
            tn_ap(10, -10, 2)
        with self.assertRaises(ValueError):
            tn_ap(10, 10, -2)
