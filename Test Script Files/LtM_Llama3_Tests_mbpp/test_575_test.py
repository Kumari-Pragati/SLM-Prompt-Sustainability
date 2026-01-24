import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_L(self):
        self.assertEqual(count_no(2, 3, 0, 10), 2)

    def test_edge_R(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_N(self):
        self.assertEqual(count_no(2, 1, 5, 10), 7)

    def test_edge_A(self):
        self.assertEqual(count_no(1, 3, 5, 10), 10)

    def test_edge_A_zero(self):
        self.assertEqual(count_no(0, 3, 5, 10), 10)

    def test_edge_N_zero(self):
        self.assertEqual(count_no(2, 0, 5, 10), 5)

    def test_edge_L_zero(self):
        self.assertEqual(count_no(2, 3, 0, 0), 2)

    def test_edge_R_zero(self):
        self.assertEqual(count_no(2, 3, 0, 0), 0)

    def test_edge_L_R(self):
        self.assertEqual(count_no(2, 3, 5, 5), 7)

    def test_edge_N_A(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_N_A_zero(self):
        self.assertEqual(count_no(0, 3, 5, 10), 10)

    def test_edge_L_A(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_R_A(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_L_R_A(self):
        self.assertEqual(count_no(2, 3, 5, 5), 7)

    def test_edge_N_L(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_N_R(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_N_L_R(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_N_L_R_A(self):
        self.assertEqual(count_no(2, 3, 5, 5), 7)

    def test_edge_N_L_R_A_zero(self):
        self.assertEqual(count_no(0, 3, 5, 5), 5)

    def test_edge_N_L_R_A_zero(self):
        self.assertEqual(count_no(0, 3, 5, 5), 5)
