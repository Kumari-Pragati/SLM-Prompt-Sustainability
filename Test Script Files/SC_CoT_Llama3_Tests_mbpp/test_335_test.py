import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(ap_sum(1, 5, 2), 9)

    def test_edge_case_n_zero(self):
        self.assertEqual(ap_sum(1, 0, 2), 1)

    def test_edge_case_a_zero(self):
        self.assertEqual(ap_sum(0, 5, 2), 0)

    def test_edge_case_d_zero(self):
        self.assertEqual(ap_sum(1, 5, 0), 5)

    def test_negative_n(self):
        self.assertEqual(ap_sum(1, -5, 2), 1)

    def test_negative_a(self):
        self.assertEqual(ap_sum(-1, 5, 2), -1)

    def test_negative_d(self):
        self.assertEqual(ap_sum(1, 5, -2), 1)

    def test_non_integer_n(self):
        self.assertEqual(ap_sum(1, 5.5, 2), 9)

    def test_non_integer_a(self):
        self.assertEqual(ap_sum(1.5, 5, 2), 9)

    def test_non_integer_d(self):
        self.assertEqual(ap_sum(1, 5, 2.5), 9)

    def test_non_integer_n_and_a(self):
        self.assertEqual(ap_sum(1.5, 5.5, 2), 9)

    def test_non_integer_n_and_d(self):
        self.assertEqual(ap_sum(1.5, 5, 2.5), 9)

    def test_non_integer_a_and_d(self):
        self.assertEqual(ap_sum(1.5, 5, 2.5), 9)

    def test_non_integer_n_and_a_and_d(self):
        self.assertEqual(ap_sum(1.5, 5.5, 2.5), 9)
