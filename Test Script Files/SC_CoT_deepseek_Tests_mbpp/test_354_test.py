import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tn_ap(5, 10, 2), 25)

    def test_boundary_conditions(self):
        self.assertEqual(tn_ap(5, 0, 2), 5)
        self.assertEqual(tn_ap(5, 10, 0), 5)

    def test_edge_cases(self):
        self.assertEqual(tn_ap(0, 10, 2), 20)
        self.assertEqual(tn_ap(5, 10, -2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tn_ap("5", 10, 2)
        with self.assertRaises(TypeError):
            tn_ap(5, "10", 2)
        with self.assertRaises(TypeError):
            tn_ap(5, 10, "2")
