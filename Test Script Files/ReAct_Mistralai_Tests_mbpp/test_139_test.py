import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_positive_numbers(self):
        """Test circle circumference with positive numbers"""
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586)
        self.assertAlmostEqual(circle_circumference(2), 12.566370614359172)
        self.assertAlmostEqual(circle_circumference(3), 18.84955592153873)

    def test_zero_and_negative_numbers(self):
        """Test circle circumference with zero and negative numbers"""
        self.assertAlmostEqual(circle_circumference(0), 0)
        self.assertRaises(ValueError, circle_circumference, -1)

    def test_large_number(self):
        """Test circle circumference with a large number"""
        self.assertAlmostEqual(circle_circumference(1000), 628318.4955592154)

    def test_small_number(self):
        """Test circle circumference with a small number"""
        self.assertAlmostEqual(circle_circumference(0.001), 0.006283185307179586)
