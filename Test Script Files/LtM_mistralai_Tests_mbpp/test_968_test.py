import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(floor_Max(1, 2, 3), 2)
        self.assertEqual(floor_Max(2, 3, 4), 6)
        self.assertEqual(floor_Max(3, 4, 5), 12)

    def test_edge_cases(self):
        self.assertEqual(floor_Max(1, 2, 1), 0)
        self.assertEqual(floor_Max(2, 2, 2), 1)
        self.assertEqual(floor_Max(3, 3, 1), 0)
        self.assertEqual(floor_Max(4, 4, 4), 4)

    def test_boundary_cases(self):
        self.assertEqual(floor_Max(1, 2, 2), 2)
        self.assertEqual(floor_Max(2, 2, 3), 4)
        self.assertEqual(floor_Max(3, 3, 4), 9)
        self.assertEqual(floor_Max(4, 4, 5), 16)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, lambda: floor_Max(-1, 2, 3))
        self.assertRaises(ValueError, lambda: floor_Max(1, -2, 3))
        self.assertRaises(ValueError, lambda: floor_Max(1, 2, -3))

    def test_zero_inputs(self):
        self.assertEqual(floor_Max(0, 2, 3), 0)
        self.assertEqual(floor_Max(1, 0, 3), 0)
        self.assertEqual(floor_Max(1, 2, 0), 0)
