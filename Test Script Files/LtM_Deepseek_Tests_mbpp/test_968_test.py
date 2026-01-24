import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(floor_Max(2, 3, 5), 2)
        self.assertEqual(floor_Max(3, 4, 6), 3)

    def test_boundary_conditions(self):
        self.assertEqual(floor_Max(1, 2, 0), 0)
        self.assertEqual(floor_Max(1, 2, 1), 0)
        self.assertEqual(floor_Max(1, 2, 2), 1)
        self.assertEqual(floor_Max(1, 2, 3), 1)

    def test_edge_cases(self):
        self.assertEqual(floor_Max(1, 2, 4), 2)
        self.assertEqual(floor_Max(1, 2, 5), 2)
        self.assertEqual(floor_Max(1, 2, 6), 2)
        self.assertEqual(floor_Max(1, 2, 7), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            floor_Max(0, 2, 5)
        with self.assertRaises(ValueError):
            floor_Max(2, 0, 5)
        with self.assertRaises(ValueError):
            floor_Max(2, 1, 0)
