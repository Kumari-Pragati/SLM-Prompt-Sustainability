import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(tn_ap(5, 10, 2), 25)

    def test_boundary_conditions(self):
        self.assertEqual(tn_ap(0, 0, 0), 0)
        self.assertEqual(tn_ap(100, 1, 0), 100)
        self.assertEqual(tn_ap(100, 0, 10), 0)

    def test_edge_cases(self):
        self.assertEqual(tn_ap(100, -1, 10), 90)
        self.assertEqual(tn_ap(100, 1, -10), 110)

    def test_more_complex_cases(self):
        self.assertEqual(tn_ap(1, 100, 1), 100)
        self.assertEqual(tn_ap(100, 100, -1), 0)
