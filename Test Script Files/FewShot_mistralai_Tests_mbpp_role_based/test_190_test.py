import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):
    def test_positive_and_finite_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 4), 6)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)
        self.assertEqual(count_Intgral_Points(2, 3, 3, 4), 6)
        self.assertEqual(count_Intgral_Points(-1, -2, 0, 0), 1)

    def test_zero_coordinates(self):
        self.assertEqual(count_Intgral_Points(0, 0, 0, 0), 0)

    def test_negative_coordinates(self):
        self.assertEqual(count_Intgral_Points(-1, -2, -3, -4), 16)
        self.assertEqual(count_Intgral_Points(-1, -2, 0, 0), 0)

    def test_infinite_coordinates(self):
        self.assertRaises(ValueError, count_Intgral_Points, float('inf'), float('inf'), float('inf'), float('inf'))
        self.assertRaises(ValueError, count_Intgral_Points, -float('inf'), -float('inf'), -float('inf'), -float('inf'))
