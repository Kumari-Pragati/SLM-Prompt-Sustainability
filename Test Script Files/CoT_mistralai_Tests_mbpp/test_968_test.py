import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(floor_Max(2, 4, 6), 4)
        self.assertEqual(floor_Max(3, 6, 9), 9)
        self.assertEqual(floor_Max(4, 8, 12), 12)

    def test_edge_case_A(self):
        self.assertEqual(floor_Max(1, 2, 2), 0)
        self.assertEqual(floor_Max(1, 3, 3), 0)

    def test_edge_case_B(self):
        self.assertEqual(floor_Max(2, 1, 1), 0)
        self.assertEqual(floor_Max(3, 1, 1), 0)

    def test_edge_case_C(self):
        self.assertEqual(floor_Max(2, 2, 1), 1)
        self.assertEqual(floor_Max(3, 3, 1), 1)

    def test_invalid_input_A(self):
        self.assertRaises(TypeError, floor_Max, 'a', 2, 3)
        self.assertRaises(TypeError, floor_Max, 2, 'b', 3)
        self.assertRaises(TypeError, floor_Max, 2, 3, 'c')

    def test_invalid_input_B(self):
        self.assertRaises(ValueError, floor_Max, 2, -1, 3)
        self.assertRaises(ValueError, floor_Max, 2, 0, 3)
