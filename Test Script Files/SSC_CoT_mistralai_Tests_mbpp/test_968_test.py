import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(floor_Max(2, 3, 5), 6)
        self.assertEqual(floor_Max(5, 3, 7), 15)
        self.assertEqual(floor_Max(10, 4, 12), 40)

    def test_edge_cases(self):
        self.assertEqual(floor_Max(2, 3, 0), 0)
        self.assertEqual(floor_Max(2, 3, 1), 2)
        self.assertEqual(floor_Max(2, 3, 2), 4)
        self.assertEqual(floor_Max(2, 3, 3), 6)

    def test_boundary_cases(self):
        self.assertEqual(floor_Max(2, 3, 4), 6)
        self.assertEqual(floor_Max(2, 3, 5), 6)
        self.assertEqual(floor_Max(2, 3, 6), 6)

    def test_invalid_input_B(self):
        self.assertRaises(ValueError, floor_Max, 2, 0, 3)
        self.assertRaises(ValueError, floor_Max, 2, -1, 3)

    def test_invalid_input_N(self):
        self.assertRaises(ValueError, floor_Max, 2, 3, -1)
        self.assertRaises(ValueError, floor_Max, 2, 3, 0)
