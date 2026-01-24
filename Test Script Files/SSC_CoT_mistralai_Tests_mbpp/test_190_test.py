import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntgralPoints(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 4), 6)
        self.assertEqual(count_Intgral_Points(-1, -2, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 0, 1), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 0)
        self.assertEqual(count_Intgral_Points(-1, -1, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(1, 1, -1, -1), 0)

    def test_negative_inputs(self):
        self.assertEqual(count_Intgral_Points(-1, -2, -3, -4), 16)
        self.assertEqual(count_Intgral_Points(-1, -2, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, -1, -1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Intgral_Points, "x1", "y1", "x2", "y2")
        self.assertRaises(TypeError, count_Intgral_Points, 1.5, 2, 3, 4)
        self.assertRaises(TypeError, count_Intgral_Points, 1, 2, "x2", 4)
        self.assertRaises(TypeError, count_Intgral_Points, 1, 2, 3, "y2")
