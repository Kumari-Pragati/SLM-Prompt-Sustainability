import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Max(3, 2, 10), 6)

    def test_boundary_case(self):
        self.assertEqual(floor_Max(1, 1, 1), 1)
        self.assertEqual(floor_Max(100, 100, 1000), 100000)

    def test_edge_case(self):
        self.assertEqual(floor_Max(0, 1, 10), 0)
        self.assertEqual(floor_Max(10, 20, 0), 0)
        self.assertEqual(floor_Max(10, 20, 1), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            floor_Max("3", 2, 10)
        with self.assertRaises(TypeError):
            floor_Max(3, "2", 10)
        with self.assertRaises(TypeError):
            floor_Max(3, 2, "10")
        with self.assertRaises(ValueError):
            floor_Max(3, 0, 10)
