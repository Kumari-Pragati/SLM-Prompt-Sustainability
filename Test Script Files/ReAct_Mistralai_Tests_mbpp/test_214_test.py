import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_positive_values(self):
        for radian in [0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]:
            result = degree_radian(radian)
            self.assertAlmostEqual(result, radian*(180/math.pi), delta=1)

    def test_negative_values(self):
        for radian in [-math.pi/2, -math.pi, -3*math.pi/2]:
            result = degree_radian(radian)
            self.assertAlmostEqual(result, radian*(180/math.pi), delta=1)

    def test_zero_value(self):
        result = degree_radian(0)
        self.assertEqual(result, 0)

    def test_large_positive_value(self):
        result = degree_radian(4*math.pi)
        self.assertEqual(result, 720)

    def test_large_negative_value(self):
        result = degree_radian(-4*math.pi)
        self.assertEqual(result, -720)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            degree_radian(None)
