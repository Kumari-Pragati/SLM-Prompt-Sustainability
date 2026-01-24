import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_floor_max_basic(self):
        self.assertEqual(floor_Max(1, 2, 3), 1)
        self.assertEqual(floor_Max(2, 3, 4), 2)
        self.assertEqual(floor_Max(3, 4, 5), 3)
        self.assertEqual(floor_Max(4, 5, 6), 4)
        self.assertEqual(floor_Max(5, 6, 7), 5)

    def test_floor_max_edge_cases(self):
        self.assertEqual(floor_Max(1, 1, 1), 0)
        self.assertEqual(floor_Max(1, 2, 1), 0)
        self.assertEqual(floor_Max(1, 2, 2), 1)
        self.assertEqual(floor_Max(1, 2, 3), 1)
        self.assertEqual(floor_Max(1, 2, 4), 2)
        self.assertEqual(floor_Max(1, 2, 5), 2)
        self.assertEqual(floor_Max(1, 2, 6), 3)
        self.assertEqual(floor_Max(1, 2, 7), 3)
        self.assertEqual(floor_Max(1, 2, 8), 4)
        self.assertEqual(floor_Max(1, 2, 9), 4)
        self.assertEqual(floor_Max(1, 2, 10), 5)

    def test_floor_max_negative(self):
        self.assertEqual(floor_Max(-1, 2, 3), 0)
        self.assertEqual(floor_Max(1, -2, 3), 0)
        self.assertEqual(floor_Max(1, 2, -3), 0)

    def test_floor_max_zero(self):
        self.assertEqual(floor_Max(0, 2, 3), 0)
        self.assertEqual(floor_Max(1, 0, 3), 0)
        self.assertEqual(floor_Max(1, 2, 0), 0)
