import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(floor_Min(10, 5, 10), 9)
        self.assertEqual(floor_Min(10, 5, 15), 14)

    def test_edge_cases(self):
        self.assertEqual(floor_Min(10, 5, 0), 0)
        self.assertEqual(floor_Min(10, 5, 1), 0)
        self.assertEqual(floor_Min(10, 5, 4), 4)

    def test_boundary_cases(self):
        self.assertEqual(floor_Min(10, 5, 5), 4)
        self.assertEqual(floor_Min(10, 5, 6), 5)

    def test_special_cases(self):
        self.assertEqual(floor_Min(10, 5, 20), 18)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            floor_Min('a', 5, 10)
        with self.assertRaises(TypeError):
            floor_Min(10, 'b', 10)
        with self.assertRaises(TypeError):
            floor_Min(10, 5, 'c')
