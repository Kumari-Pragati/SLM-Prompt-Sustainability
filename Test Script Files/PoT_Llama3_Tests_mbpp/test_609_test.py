import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(10, 2, 5), 9)

    def test_edge_case_A(self):
        self.assertEqual(floor_Min(1, 2, 5), 0)

    def test_edge_case_B(self):
        self.assertEqual(floor_Min(10, 2, 1), 0)

    def test_edge_case_N(self):
        self.assertEqual(floor_Min(10, 2, 2), 1)

    def test_edge_case_B_N(self):
        self.assertEqual(floor_Min(10, 2, 2), 1)

    def test_edge_case_A_B(self):
        self.assertEqual(floor_Min(1, 1, 5), 0)

    def test_edge_case_A_B_N(self):
        self.assertEqual(floor_Min(1, 1, 2), 0)

    def test_edge_case_A_B_N_B(self):
        self.assertEqual(floor_Min(1, 1, 1), 0)

    def test_edge_case_A_B_N_B_N(self):
        self.assertEqual(floor_Min(1, 1, 1), 0)

    def test_edge_case_A_B_N_B_N_B(self):
        self.assertEqual(floor_Min(1, 1, 1), 0)
