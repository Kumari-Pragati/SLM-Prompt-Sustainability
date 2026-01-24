import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(circle_circumference(3), 18.849555921538738)

    def test_zero_input(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_negative_input(self):
        self.assertRaises(ValueError, circle_circumference, -1)

    def test_large_input(self):
        self.assertAlmostEqual(circle_circumference(10000), 628318.4955592154)

    def test_float_input(self):
        self.assertAlmostEqual(circle_circumference(2.5), 15.707963267948966)
