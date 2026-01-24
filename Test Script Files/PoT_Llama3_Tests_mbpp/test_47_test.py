import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(compute_Last_Digit(1, 2), 1)

    def test_edge_case_A_equals_B(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)

    def test_edge_case_B_A_plus_5(self):
        self.assertEqual(compute_Last_Digit(1, 6), 0)

    def test_edge_case_B_A_minus_5(self):
        self.assertEqual(compute_Last_Digit(1, 4), 1)

    def test_edge_case_A_B_minus_5(self):
        self.assertEqual(compute_Last_Digit(4, 1), 1)

    def test_edge_case_A_B_plus_5(self):
        self.assertEqual(compute_Last_Digit(4, 9), 0)

    def test_edge_case_A_B_minus_10(self):
        self.assertEqual(compute_Last_Digit(4, -6), 1)

    def test_edge_case_A_B_plus_10(self):
        self.assertEqual(compute_Last_Digit(4, 14), 0)

    def test_edge_case_A_B_minus_20(self):
        self.assertEqual(compute_Last_Digit(4, -16), 1)

    def test_edge_case_A_B_plus_20(self):
        self.assertEqual(compute_Last_Digit(4, 24), 0)

    def test_edge_case_A_B_minus_30(self):
        self.assertEqual(compute_Last_Digit(4, -26), 1)

    def test_edge_case_A_B_plus_30(self):
        self.assertEqual(compute_Last_Digit(4, 34), 0)

    def test_edge_case_A_B_minus_40(self):
        self.assertEqual(compute_Last_Digit(4, -36), 1)

    def test_edge_case_A_B_plus_40(self):
        self.assertEqual(compute_Last_Digit(4, 44), 0)

    def test_edge_case_A_B_minus_50(self):
        self.assertEqual(compute_Last_Digit(4, -46), 1)

    def test_edge_case_A_B_plus_50(self):
        self.assertEqual(compute_Last_Digit(4, 54), 0)

    def test_edge_case_A_B_minus_60(self):
        self.assertEqual(compute_Last_Digit(4, -58), 1)

    def test_edge_case_A_B_plus_60(self):
        self.assertEqual(compute_Last_Digit(4, 64), 0)

    def test_edge_case_A_B_minus_70(self):
        self.assertEqual(compute_Last_Digit(4, -68), 1)

    def test_edge_case_A_B_plus_70(self):
        self.assertEqual(compute_Last_Digit(4, 74), 0)

    def test_edge_case_A_B_minus_80(self):
        self.assertEqual(compute_Last_Digit(4, -78), 1)

    def test_edge_case_A_B_plus_80(self):
        self.assertEqual(compute_Last_Digit(4, 84), 0)

    def test_edge_case_A_B_minus_90(self):
        self.assertEqual(compute_Last_Digit(4, -88), 1)

    def test_edge_case_A_B_plus_90(self):
        self.assertEqual(compute_Last_Digit(4, 94), 0)

    def test_edge_case_A_B_minus_100(self):
        self.assertEqual(compute_Last_Digit(4, -98), 1)

    def test_edge_case_A_B_plus_100(self):
        self.assertEqual(compute_Last_Digit(4, 104), 0)
