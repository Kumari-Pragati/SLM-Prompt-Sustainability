import unittest
from609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_floor_min_basic(self):
        self.assertEqual(floor_Min(1, 2, 3), 1)
        self.assertEqual(floor_Min(2, 3, 4), 2)
        self.assertEqual(floor_Min(3, 4, 5), 3)
        self.assertEqual(floor_Min(4, 5, 6), 4)
        self.assertEqual(floor_Min(5, 6, 7), 5)

    def test_floor_min_edge_cases(self):
        self.assertEqual(floor_Min(1, 1, 1), 1)
        self.assertEqual(floor_Min(1, 1, 2), 1)
        self.assertEqual(floor_Min(1, 2, 1), 0)
        self.assertEqual(floor_Min(2, 2, 1), 1)
        self.assertEqual(floor_Min(2, 3, 2), 2)
        self.assertEqual(floor_Min(3, 3, 2), 3)
        self.assertEqual(floor_Min(3, 4, 3), 3)
        self.assertEqual(floor_Min(4, 4, 3), 4)
        self.assertEqual(floor_Min(4, 5, 4), 4)
        self.assertEqual(floor_Min(5, 5, 4), 5)
