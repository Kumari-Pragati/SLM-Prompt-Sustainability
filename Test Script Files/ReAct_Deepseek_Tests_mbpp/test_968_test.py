import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Max(10, 3, 10), 30)

    def test_typical_case_2(self):
        self.assertEqual(floor_Max(5, 2, 10), 25)

    def test_boundary_case_B_minus_1(self):
        self.assertEqual(floor_Max(10, 1, 10), 10)

    def test_boundary_case_N(self):
        self.assertEqual(floor_Max(10, 3, 0), 0)

    def test_edge_case_B_equals_1(self):
        self.assertEqual(floor_Max(10, 1, 10), 10)

    def test_edge_case_A_equals_0(self):
        self.assertEqual(floor_Max(0, 3, 10), 0)

    def test_edge_case_N_less_than_B_minus_1(self):
        self.assertEqual(floor_Max(10, 3, 2), 20)

    def test_edge_case_N_equals_B_minus_1(self):
        self.assertEqual(floor_Max(10, 3, 2), 20)

    def test_edge_case_N_equals_B(self):
        self.assertEqual(floor_Max(10, 3, 3), 30)
