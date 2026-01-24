import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(floor_Min(1, 2, 1), 2)
        self.assertEqual(floor_Min(2, 3, 2), 6)
        self.assertEqual(floor_Min(3, 4, 3), 12)

    def test_edge_cases(self):
        self.assertEqual(floor_Min(1, 2, 0), 0)
        self.assertEqual(floor_Min(1, 2, 2), 2)
        self.assertEqual(floor_Min(1, 1, 1), 1)
        self.assertEqual(floor_Min(1, 1, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(floor_Min(sys.maxsize, 1, 1), sys.maxsize)
        self.assertEqual(floor_Min(1, sys.maxsize, 1), sys.maxsize)
        self.assertEqual(floor_Min(sys.maxsize, sys.maxsize, 1), sys.maxsize)

    def test_negative_numbers(self):
        self.assertEqual(floor_Min(-1, 2, 1), -2)
        self.assertEqual(floor_Min(1, -2, 1), 2)
        self.assertEqual(floor_Min(-1, -2, 1), 1)
