import unittest
from190_code import count_Intgral_Points

class TestCountIntgralPoints(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 4), 6)
        self.assertEqual(count_Intgral_Points(-1, -2, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 1)

    def test_zero_values(self):
        self.assertEqual(count_Intgral_Points(0, 0, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 0, 1), 0)
        self.assertEqual(count_Intgral_Points(1, 0, 1, 0), 0)

    def test_negative_values(self):
        self.assertEqual(count_Intgral_Points(-1, -2, -3, -4), 20)
        self.assertEqual(count_Intgral_Points(-1, -2, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, -1, -1), 0)
        self.assertEqual(count_Intgral_Points(-1, -1, -2, -2), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 1)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 3), 2)
        self.assertEqual(count_Intgral_Points(1, 1, 2, -1), 2)
        self.assertEqual(count_Intgral_Points(1, 1, -1, 1), 2)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Intgral_Points, 'a', 'b', 'c', 'd')
        self.assertRaises(TypeError, count_Intgral_Points, 1, 'b', 2, 3)
        self.assertRaises(TypeError, count_Intgral_Points, 1, 2, 'c', 3)
        self.assertRaises(TypeError, count_Intgral_Points, 1, 2, 3, 'd')
