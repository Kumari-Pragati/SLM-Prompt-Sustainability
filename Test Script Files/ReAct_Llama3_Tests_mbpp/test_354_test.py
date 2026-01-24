import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tn_ap(2, 4, 1), 7)

    def test_edge_case_n_zero(self):
        self.assertEqual(tn_ap(2, 0, 1), 2)

    def test_edge_case_d_zero(self):
        self.assertEqual(tn_ap(2, 4, 0), 2)

    def test_edge_case_a_zero(self):
        self.assertEqual(tn_ap(0, 4, 1), 4)

    def test_edge_case_n_one(self):
        self.assertEqual(tn_ap(2, 1, 1), 3)

    def test_edge_case_d_negative(self):
        self.assertEqual(tn_ap(2, 4, -1), 2)

    def test_edge_case_a_negative(self):
        self.assertEqual(tn_ap(-2, 4, 1), -2)

    def test_edge_case_n_negative(self):
        self.assertEqual(tn_ap(2, -4, 1), 2)

    def test_edge_case_d_zero_and_n_zero(self):
        self.assertEqual(tn_ap(2, 0, 0), 2)

    def test_edge_case_a_zero_and_d_zero(self):
        self.assertEqual(tn_ap(0, 0, 0), 0)

    def test_edge_case_a_zero_and_n_zero(self):
        self.assertEqual(tn_ap(0, 0, 0), 0)
