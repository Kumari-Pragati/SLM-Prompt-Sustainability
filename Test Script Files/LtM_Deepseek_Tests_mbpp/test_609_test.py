import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(floor_Min(2, 3, 1), 2)
        self.assertEqual(floor_Min(3, 4, 2), 3)

    def test_boundary_conditions(self):
        self.assertEqual(floor_Min(1, 1, 0), 0)
        self.assertEqual(floor_Min(1, 2, 1), 1)
        self.assertEqual(floor_Min(1, 2, 2), 1)

    def test_edge_cases(self):
        self.assertEqual(floor_Min(0, 1, 0), 0)
        self.assertEqual(floor_Min(0, 1, 1), 0)
        self.assertEqual(floor_Min(2, 3, 3), 2)
        self.assertEqual(floor_Min(2, 3, 4), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            floor_Min("2", 3, 1)
        with self.assertRaises(TypeError):
            floor_Min(2, "3", 1)
        with self.assertRaises(TypeError):
            floor_Min(2, 3, "1")
        with self.assertRaises(ValueError):
            floor_Min(2, 0, 1)
