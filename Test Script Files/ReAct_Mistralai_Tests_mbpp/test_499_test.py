import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):

    def test_positive_integer(self):
        """Test diameter calculation for positive integers"""
        self.assertEqual(diameter_circle(3), 6)
        self.assertEqual(diameter_circle(5), 10)

    def test_zero(self):
        """Test diameter calculation for zero"""
        self.assertEqual(diameter_circle(0), 0)

    def test_negative_number(self):
        """Test diameter calculation for negative numbers"""
        self.assertRaises(ValueError, diameter_circle, -1)

    def test_float(self):
        """Test diameter calculation for floats"""
        self.assertAlmostEqual(diameter_circle(3.5), 7)

    def test_non_numeric(self):
        """Test diameter calculation for non-numeric inputs"""
        self.assertRaises(TypeError, diameter_circle, 'str')
        self.assertRaises(TypeError, diameter_circle, [1, 2, 3])
