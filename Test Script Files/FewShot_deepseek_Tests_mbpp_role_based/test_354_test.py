import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tn_ap(5, 10, 2), 25)

    def test_edge_condition(self):
        self.assertEqual(tn_ap(5, 1, 2), 5)

    def test_boundary_condition(self):
        self.assertEqual(tn_ap(5, 0, 2), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tn_ap("5", 10, 2)
        with self.assertRaises(TypeError):
            tn_ap(5, "10", 2)
        with self.assertRaises(TypeError):
            tn_ap(5, 10, "2")
