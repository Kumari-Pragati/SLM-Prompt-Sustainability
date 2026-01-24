import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_floor_min(self):
        self.assertEqual(floor_Min(5, 3, 10), 15)
        self.assertEqual(floor_Min(10, 2, 5), 10)
        self.assertEqual(floor_Min(5, 5, 10), 25)
        self.assertEqual(floor_Min(10, 10, 5), 50)
        self.assertEqual(floor_Min(5, 1, 10), 5)
        self.assertEqual(floor_Min(10, 1, 5), 5)

    def test_floor_min_edge_cases(self):
        self.assertEqual(floor_Min(0, 0, 0), 0)
        self.assertEqual(floor_Min(0, 1, 0), 0)
        self.assertEqual(floor_Min(1, 0, 0), 0)
        self.assertEqual(floor_Min(1, 1, 0), 0)
