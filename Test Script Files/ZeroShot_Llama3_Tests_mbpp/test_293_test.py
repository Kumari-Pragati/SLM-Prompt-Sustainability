import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_positive_values(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, 12), 13.0)
        self.assertAlmostEqual(otherside_rightangle(7, 24), 25.0)

    def test_zero_values(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)
        self.assertAlmostEqual(otherside_rightangle(0, 3), 3.0)
        self.assertAlmostEqual(otherside_rightangle(3, 0), 3.0)

    def test_negative_values(self):
        self.assertAlmostEqual(otherside_rightangle(-3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, -12), 13.0)
        self.assertAlmostEqual(otherside_rightangle(-7, 24), 25.0)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            otherside_rightangle('a', 4)
        with self.assertRaises(TypeError):
            otherside_rightangle(3, 'b')
