import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(floor_Min(10, 3, 2), 20)
        self.assertEqual(floor_Min(5, 7, 10), 50)
        self.assertEqual(floor_Min(15, 4, 3), 60)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(floor_Min(0, 5, 10), 0)
        self.assertEqual(floor_Min(10, 0, 2), 0)
        self.assertEqual(floor_Min(10, 1, 10), 10)

    def test_corner_cases(self):
        self.assertEqual(floor_Min(10, 2, 0), 0)
        self.assertEqual(floor_Min(10, 2, 1), 10)
        self.assertEqual(floor_Min(10, 2, 2), 20)
