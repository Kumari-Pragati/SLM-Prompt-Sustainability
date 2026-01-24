import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tn_ap(2, 5, 1), 8)

    def test_edge_case(self):
        self.assertEqual(tn_ap(2, 1, 1), 2)

    def test_zero_n(self):
        self.assertEqual(tn_ap(2, 0, 1), 2)

    def test_zero_a(self):
        self.assertEqual(tn_ap(0, 5, 1), 5)

    def test_negative_n(self):
        self.assertEqual(tn_ap(2, -5, 1), 2)

    def test_negative_d(self):
        self.assertEqual(tn_ap(2, 5, -1), 2)

    def test_non_integer_n(self):
        self.assertEqual(tn_ap(2, 5.5, 1), 8)

    def test_non_integer_d(self):
        self.assertEqual(tn_ap(2, 5, 1.5), 8)

    def test_non_integer_a(self):
        self.assertEqual(tn_ap(2.5, 5, 1), 8)
