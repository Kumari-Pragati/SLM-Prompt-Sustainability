import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(ap_sum(1, 5, 2), 9)

    def test_edge_case_n_zero(self):
        self.assertEqual(ap_sum(1, 0, 2), 1)

    def test_edge_case_d_zero(self):
        self.assertEqual(ap_sum(1, 5, 0), 5)

    def test_edge_case_a_zero(self):
        self.assertEqual(ap_sum(0, 5, 2), 0)

    def test_edge_case_n_one(self):
        self.assertEqual(ap_sum(1, 1, 2), 2)

    def test_edge_case_d_negative(self):
        self.assertEqual(ap_sum(1, 5, -2), -3)

    def test_edge_case_a_negative(self):
        self.assertEqual(ap_sum(-1, 5, 2), -3)

    def test_edge_case_n_large(self):
        self.assertEqual(ap_sum(1, 100, 2), 9900)

    def test_edge_case_d_large(self):
        self.assertEqual(ap_sum(1, 5, 100), 9900)

    def test_edge_case_a_large(self):
        self.assertEqual(ap_sum(100, 5, 2), 9900)
