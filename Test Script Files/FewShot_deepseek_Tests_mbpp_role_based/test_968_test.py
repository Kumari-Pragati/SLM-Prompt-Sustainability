import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(floor_Max(5, 3, 10), 15)

    def test_boundary_condition(self):
        self.assertEqual(floor_Max(5, 3, 0), 0)

    def test_edge_condition(self):
        self.assertEqual(floor_Max(5, 3, 1), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            floor_Max("5", 3, 10)
