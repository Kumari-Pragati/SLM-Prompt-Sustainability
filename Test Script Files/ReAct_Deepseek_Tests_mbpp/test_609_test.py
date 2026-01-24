import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(10, 3, 5), 30)

    def test_edge_case_with_zero_B(self):
        self.assertEqual(floor_Min(10, 0, 5), 0)

    def test_edge_case_with_negative_A(self):
        self.assertEqual(floor_Min(-10, 3, 5), -30)

    def test_edge_case_with_negative_B(self):
        self.assertEqual(floor_Min(10, -3, 5), 30)

    def test_edge_case_with_negative_N(self):
        self.assertEqual(floor_Min(10, 3, -5), 0)

    def test_edge_case_with_large_N(self):
        self.assertEqual(floor_Min(10, 3, 1000), 3330)

    def test_edge_case_with_large_A(self):
        self.assertEqual(floor_Min(10000, 3, 5), 16666666)

    def test_edge_case_with_large_A_and_large_N(self):
        self.assertEqual(floor_Min(10000, 3, 1000), 333333330)
