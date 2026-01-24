import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586)
        self.assertAlmostEqual(circle_circumference(2), 12.566370614359172)
        self.assertAlmostEqual(circle_circumference(3), 18.849555921538734)

    def test_zero(self):
        self.assertEqual(circle_circumference(0), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(circle_circumference(-1), -6.283185307179586)
        self.assertAlmostEqual(circle_circumference(-2), -12.566370614359172)
        self.assertAlmostEqual(circle_circumference(-3), -18.849555921538734)

    def test_non_numeric_inputs(self):
        self.assertRaises(TypeError, circle_circumference, "not a number")
        self.assertRaises(TypeError, circle_circumference, None)
        self.assertRaises(TypeError, circle_circumference, [1, 2, 3])
