import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(1, 3, 4), 3)
        self.assertEqual(floor_Min(2, 4, 5), 10)
        self.assertEqual(floor_Min(3, 6, 7), 18)

    def test_edge_case_small_B(self):
        self.assertEqual(floor_Min(1, 1, 2), 1)
        self.assertEqual(floor_Min(2, 2, 3), 4)

    def test_edge_case_large_N(self):
        self.assertEqual(floor_Min(1, 2, 32), 32)
        self.assertEqual(floor_Min(2, 3, 64), 192)

    def test_edge_case_N_equal_B(self):
        self.assertEqual(floor_Min(1, 1, 1), 1)
        self.assertEqual(floor_Min(2, 2, 2), 2)

    def test_corner_case_N_zero(self):
        self.assertEqual(floor_Min(1, 2, 0), 0)
        self.assertEqual(floor_Min(2, 3, 0), 0)
