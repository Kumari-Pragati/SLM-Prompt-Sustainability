import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_positive_degrees(self):
        """Test correct calculation for positive degrees"""
        self.assertAlmostEqual(arc_length(10, 90), 28.274333882308138)
        self.assertAlmostEqual(arc_length(10, 180), 56.54822574719958)
        self.assertAlmostEqual(arc_length(10, 270), 56.54822574719958)

    def test_zero_degrees(self):
        """Test correct calculation for zero degrees"""
        self.assertEqual(arc_length(10, 0), 0)

    def test_negative_degrees(self):
        """Test correct calculation for negative degrees"""
        self.assertAlmostEqual(arc_length(10, -90), 28.274333882308138)

    def test_degrees_greater_than_360(self):
        """Test None return for degrees greater than 360"""
        self.assertIsNone(arc_length(10, 400))

    def test_negative_diameter(self):
        """Test None return for negative diameter"""
        self.assertIsNone(arc_length(-10, 90))

    def test_zero_diameter(self):
        """Test zero return for zero diameter"""
        self.assertEqual(arc_length(0, 90), 0)
