import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(floor_Min(10, 2, 5), 9)
        self.assertEqual(floor_Min(5, 3, 2), 4)
        self.assertEqual(floor_Min(20, 4, 8), 16)

    def test_edge_cases(self):
        self.assertEqual(floor_Min(10, 2, 0), 0)
        self.assertEqual(floor_Min(5, 3, 3), 4)
        self.assertEqual(floor_Min(20, 4, 20), 16)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            floor_Min('a', 2, 5)
        with self.assertRaises(TypeError):
            floor_Min(10, 'b', 5)
        with self.assertRaises(TypeError):
            floor_Min(10, 2, 'c')

    def test_boundary_conditions(self):
        self.assertEqual(floor_Min(10, 2, 1), 0)
        self.assertEqual(floor_Min(10, 2, 10), 9)
