import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(floor_Max(2, 3, 5), 2)
        self.assertEqual(floor_Max(5, 3, 5), 5)
        self.assertEqual(floor_Max(10, 2, 5), 5)

    def test_edge_cases(self):
        self.assertEqual(floor_Max(0, 3, 5), 0)
        self.assertEqual(floor_Max(5, 0, 5), 0)
        self.assertEqual(floor_Max(5, 5, 5), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            floor_Max('a', 3, 5)
        with self.assertRaises(TypeError):
            floor_Max(2, 'b', 5)
        with self.assertRaises(TypeError):
            floor_Max(2, 3, 'c')

    def test_boundary_conditions(self):
        self.assertEqual(floor_Max(5, 5, 5), 5)
        self.assertEqual(floor_Max(5, 4, 5), 4)
        self.assertEqual(floor_Max(5, 3, 5), 3)
