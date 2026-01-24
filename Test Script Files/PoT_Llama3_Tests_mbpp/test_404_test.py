import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(minimum(1, 2), 1)

    def test_edge_case_a_eq_b(self):
        self.assertEqual(minimum(2, 2), 2)

    def test_edge_case_b_eq_a(self):
        self.assertEqual(minimum(2, 3), 2)

    def test_edge_case_a_greater_b(self):
        self.assertEqual(minimum(4, 3), 3)

    def test_edge_case_b_greater_a(self):
        self.assertEqual(minimum(3, 4), 3)

    def test_edge_case_a_eq_b_eq_zero(self):
        self.assertEqual(minimum(0, 0), 0)

    def test_edge_case_a_eq_b_eq_negative(self):
        self.assertEqual(minimum(-1, -1), -1)

    def test_edge_case_a_greater_b_eq_zero(self):
        self.assertEqual(minimum(0, -1), -1)

    def test_edge_case_b_greater_a_eq_zero(self):
        self.assertEqual(minimum(-1, 0), -1)
