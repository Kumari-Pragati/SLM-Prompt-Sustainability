import unittest
from mbpp_609_code import divmod

from609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(floor_Min(2, 3, 4), 6)
        self.assertEqual(floor_Min(3, 4, 5), 12)
        self.assertEqual(floor_Min(4, 5, 6), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(floor_Min(0, 1, 0), 0)
        self.assertEqual(floor_Min(1, 1, 0), 0)
        self.assertEqual(floor_Min(1, 1, 1), 1)
        self.assertEqual(floor_Min(1, 2, 0), 0)
        self.assertEqual(floor_Min(1, 2, 1), 1)
        self.assertEqual(floor_Min(1, 2, 2), 2)
        self.assertEqual(floor_Min(1, 3, 0), 0)
        self.assertEqual(floor_Min(1, 3, 1), 1)
        self.assertEqual(floor_Min(1, 3, 2), 3)
        self.assertEqual(floor_Min(1, 4, 0), 0)
        self.assertEqual(floor_Min(1, 4, 1), 1)
        self.assertEqual(floor_Min(1, 4, 2), 4)
        self.assertEqual(floor_Min(1, 5, 0), 0)
        self.assertEqual(floor_Min(1, 5, 1), 1)
        self.assertEqual(floor_Min(1, 5, 2), 5)
        self.assertEqual(floor_Min(1, 6, 0), 0)
        self.assertEqual(floor_Min(1, 6, 1), 1)
        self.assertEqual(floor_Min(1, 6, 2), 6)
        self.assertEqual(floor_Min(1, 7, 0), 0)
        self.assertEqual(floor_Min(1, 7, 1), 1)
        self.assertEqual(floor_Min(1, 7, 2), 7)
        self.assertEqual(floor_Min(1, 8, 0), 0)
        self.assertEqual(floor_Min(1, 8, 1), 1)
        self.assertEqual(floor_Min(1, 8, 2), 8)
        self.assertEqual(floor_Min(1, 9, 0), 0)
        self.assertEqual(floor_Min(1, 9, 1), 1)
        self.assertEqual(floor_Min(1, 9, 2), 9)
        self.assertEqual(floor_Min(1, 10, 0), 0)
        self.assertEqual(floor_Min(1, 10, 1), 1)
        self.assertEqual(floor_Min(1, 10, 2), 10)
