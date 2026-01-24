import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(floor_Max(10, 5, 10), 9)

    def test_edge_case_A(self):
        self.assertEqual(floor_Max(1, 5, 10), 0)

    def test_edge_case_B(self):
        self.assertEqual(floor_Max(10, 1, 10), 9)

    def test_edge_case_N(self):
        self.assertEqual(floor_Max(10, 5, 1), 0)

    def test_edge_case_B_N(self):
        self.assertEqual(floor_Max(10, 10, 10), 9)

    def test_edge_case_A_B(self):
        self.assertEqual(floor_Max(1, 1, 10), 0)

    def test_edge_case_A_N(self):
        self.assertEqual(floor_Max(1, 5, 0), 0)

    def test_edge_case_B_N(self):
        self.assertEqual(floor_Max(10, 5, 0), 0)
