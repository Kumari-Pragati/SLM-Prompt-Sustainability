import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Jumps(5, 10, 15), 1.5)

    def test_edge_case_d_zero(self):
        self.assertEqual(min_Jumps(5, 10, 0), 0)

    def test_edge_case_d_equal_a(self):
        self.assertEqual(min_Jumps(5, 10, 5), 1)

    def test_edge_case_d_equal_b(self):
        self.assertEqual(min_Jumps(5, 10, 10), 2)

    def test_edge_case_d_greater_than_b(self):
        self.assertEqual(min_Jumps(5, 10, 15), 2)

    def test_edge_case_d_greater_than_a_and_b(self):
        self.assertEqual(min_Jumps(5, 10, 20), 2)

    def test_edge_case_a_greater_than_b(self):
        self.assertEqual(min_Jumps(10, 5, 15), 2)

    def test_edge_case_b_greater_than_a(self):
        self.assertEqual(min_Jumps(5, 10, 15), 2)
