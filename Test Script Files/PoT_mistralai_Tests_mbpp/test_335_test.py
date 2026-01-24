import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(ap_sum(1, 5, 2), 25)

    def test_edge_case_a(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)

    def test_edge_case_b(self):
        self.assertEqual(ap_sum(1, 1, 0), 1)

    def test_edge_case_c(self):
        self.assertEqual(ap_sum(1, 0, 1), 0)

    def test_boundary_case_a(self):
        self.assertEqual(ap_sum(1, 1, 1), 2)

    def test_boundary_case_b(self):
        self.assertEqual(ap_sum(1, 2, 1), 6)
