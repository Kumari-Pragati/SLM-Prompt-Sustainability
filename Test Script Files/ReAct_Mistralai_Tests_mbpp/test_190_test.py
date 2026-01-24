import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 5), 12)
        self.assertEqual(count_Intgral_Points(0, 0, 4, 4), 16)
        self.assertEqual(count_Intgral_Points(-1, -1, 2, 3), 6)

    def test_zero_values(self):
        self.assertEqual(count_Intgral_Points(0, 0, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 0, 1), 0)

    def test_negative_values(self):
        self.assertEqual(count_Intgral_Points(-3, -2, -1, -4), 16)
        self.assertEqual(count_Intgral_Points(-1, -1, -3, -5), 15)
        self.assertEqual(count_Intgral_Points(-2, -3, -4, -5), 24)

    def test_edge_cases(self):
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 3)
        self.assertEqual(count_Intgral_Points(1, 1, 1, 2), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 1), 0)

    def test_invalid_input(self):
        self.assertRaises(ValueError, count_Intgral_Points, -1, 'x', 1, 1)
        self.assertRaises(ValueError, count_Intgral_Points, 1, -1, 1, 'y')
        self.assertRaises(ValueError, count_Intgral_Points, 'x', 1, 1, 1)
        self.assertRaises(ValueError, count_Intgral_Points, 1, 1, 'y', 1)
