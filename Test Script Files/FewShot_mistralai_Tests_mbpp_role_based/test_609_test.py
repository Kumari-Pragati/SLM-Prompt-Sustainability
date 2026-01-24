import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(floor_Min(3, 4, 6), 6)
        self.assertEqual(floor_Min(5, 6, 10), 10)
        self.assertEqual(floor_Min(7, 8, 12), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(floor_Min(0, 1, 0), 0)
        self.assertEqual(floor_Min(1, 1, 1), 1)
        self.assertEqual(floor_Min(2, 2, 2), 2)
        self.assertEqual(floor_Min(3, 2, 0), 0)
        self.assertEqual(floor_Min(4, 2, 1), 2)
        self.assertEqual(floor_Min(5, 2, 2), 5)
        self.assertEqual(floor_Min(6, 2, 3), 6)
        self.assertEqual(floor_Min(7, 2, 4), 14)
        self.assertEqual(floor_Min(8, 2, 5), 16)
        self.assertEqual(floor_Min(9, 2, 6), 18)
