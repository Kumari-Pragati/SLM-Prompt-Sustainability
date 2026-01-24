import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(circle_circumference(5), 31.415, places=3)

    def test_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_circumference(-5)

    def test_large_radius(self):
        self.assertAlmostEqual(circle_circumference(1000), 6283.0, places=1)

    def test_float_radius(self):
        self.assertAlmostEqual(circle_circumference(3.5), 21.9735, places=3)
