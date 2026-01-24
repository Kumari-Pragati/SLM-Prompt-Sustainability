import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(floor_Max(1, 3, 5), 3)
        self.assertEqual(floor_Max(2, 4, 6), 12)
        self.assertEqual(floor_Max(3, 5, 7), 15)

    def test_edge_case_small_A(self):
        self.assertEqual(floor_Max(1, 2, 1), 1)
        self.assertEqual(floor_Max(1, 3, 0), 0)
        self.assertEqual(floor_Max(1, 4, -1), 0)

    def test_edge_case_small_B(self):
        self.assertEqual(floor_Max(2, 1, 1), 2)
        self.assertEqual(floor_Max(3, 2, 0), 0)
        self.assertEqual(floor_Max(4, 3, -1), 0)

    def test_edge_case_small_N(self):
        self.assertEqual(floor_Max(1, 2, 0), 0)
        self.assertEqual(floor_Max(2, 3, -1), 0)
        self.assertEqual(floor_Max(3, 4, -2), 0)
