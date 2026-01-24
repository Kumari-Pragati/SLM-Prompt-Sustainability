import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(floor_Max(10, 20, 30), 150)

    def test_edge_case_A(self):
        self.assertEqual(floor_Max(0, 20, 30), 0)

    def test_edge_case_B(self):
        self.assertEqual(floor_Max(10, 0, 30), 0)

    def test_edge_case_C(self):
        self.assertEqual(floor_Max(10, 20, 0), 0)

    def test_edge_case_D(self):
        self.assertEqual(floor_Max(10, 20, 1), 0)

    def test_edge_case_E(self):
        self.assertEqual(floor_Max(10, 20, 20), 180)

    def test_edge_case_F(self):
        self.assertEqual(floor_Max(10, 20, 21), 180)

    def test_edge_case_G(self):
        self.assertEqual(floor_Max(10, 20, 30), 150)

    def test_edge_case_H(self):
        self.assertEqual(floor_Max(10, 20, 31), 150)

    def test_edge_case_I(self):
        self.assertEqual(floor_Max(10, 20, 32), 150)

    def test_edge_case_J(self):
        self.assertEqual(floor_Max(10, 20, 33), 150)

    def test_edge_case_K(self):
        self.assertEqual(floor_Max(10, 20, 34), 150)

    def test_edge_case_L(self):
        self.assertEqual(floor_Max(10, 20, 35), 150)

    def test_edge_case_M(self):
        self.assertEqual(floor_Max(10, 20, 36), 150)

    def test_edge_case_N(self):
        self.assertEqual(floor_Max(10, 20, 37), 150)

    def test_edge_case_O(self):
        self.assertEqual(floor_Max(10, 20, 38), 150)

    def test_edge_case_P(self):
        self.assertEqual(floor_Max(10, 20, 39), 150)

    def test_edge_case_Q(self):
        self.assertEqual(floor_Max(10, 20, 40), 150)

    def test_edge_case_R(self):
        self.assertEqual(floor_Max(10, 20, 41), 150)

    def test_edge_case_S(self):
        self.assertEqual(floor_Max(10, 20, 42), 150)

    def test_edge_case_T(self):
        self.assertEqual(floor_Max(10, 20, 43), 150)

    def test_edge_case_U(self):
        self.assertEqual(floor_Max(10, 20, 44), 150)

    def test_edge_case_V(self):
        self.assertEqual(floor_Max(10, 20, 45), 150)

    def test_edge_case_W(self):
        self.assertEqual(floor_Max(10, 20, 46), 150)

    def test_edge_case_X(self):
        self.assertEqual(floor_Max(10, 20, 47), 150)

    def test_edge_case_Y(self):
        self.assertEqual(floor_Max(10, 20, 48), 150)

    def test_edge_case_Z(self):
        self.assertEqual(floor_Max(10, 20, 49), 150)

    def test_edge_case_AA(self):
        self.assertEqual(floor_Max(10, 20, 50), 150)

    def test_edge_case_BB(self):
        self.assertEqual(floor_Max(10, 20, 51), 150)

    def test_edge_case_CC(self):
        self.assertEqual(floor_Max(10, 20, 52), 150)

    def test_edge_case_DD(self):
        self.assertEqual(floor_Max(10, 20, 53), 150)

    def test_edge_case_EE(self):
        self.assertEqual(floor_Max(10, 20, 54), 150)

    def test_edge_case_FF(self):
        self.assertEqual(floor_Max(10, 20, 55), 150)

    def test_edge_case_GG(self):
        self.assertEqual(floor_Max(10, 20, 56), 150)

    def test_edge_case_HH(self):
        self.assertEqual(floor_Max(10, 20, 57), 150)

    def test_edge_case_II(self):
        self.assertEqual(floor_Max(10, 20, 58), 150)

    def test_edge_case_JJ(self):
        self.assertEqual(floor_Max(10, 20, 59), 150)

    def test_edge_case_KK(self):
        self.assertEqual(floor_Max(10, 20, 60), 150)

    def test_edge_case_LL(self):
        self.assertEqual(floor_Max(10, 20, 61), 150)

    def test_edge_case_MM(self):
        self.assertEqual(floor_Max(10, 20, 62),