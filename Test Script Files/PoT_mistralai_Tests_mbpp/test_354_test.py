import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tn_ap(1, 3, 2), 7)

    def test_edge_case_zero_n(self):
        self.assertEqual(tn_ap(1, 0, 2), 1)

    def test_edge_case_negative_n(self):
        self.assertEqual(tn_ap(1, -1, 2), -1)

    def test_edge_case_zero_d(self):
        self.assertEqual(tn_ap(1, 3, 0), 1)

    def test_edge_case_negative_d(self):
        self.assertEqual(tn_ap(1, 3, -2), 3)
