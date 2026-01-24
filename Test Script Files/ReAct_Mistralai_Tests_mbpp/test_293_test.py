import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightAngle(unittest.TestCase):

    def test_positive_squares(self):
        """Test positive square inputs"""
        for side in [2, 3, 4, 5]:
            self.assertEqual(otherside_rightangle(side, side), 5 * side)

    def test_positive_non_square(self):
        """Test positive non-square inputs"""
        for side1 in [2, 3, 4]:
            for side2 in [side1 + 1, side1 - 1]:
                self.assertNotEqual(otherside_rightangle(side1, side2), side1 * side2)

    def test_negative_input(self):
        """Test negative inputs"""
        self.assertRaises(ValueError, otherside_rightangle, -1, 2)
        self.assertRaises(ValueError, otherside_rightangle, 2, -1)

    def test_zero_input(self):
        """Test zero inputs"""
        self.assertRaises(ValueError, otherside_rightangle, 0, 2)
        self.assertRaises(ValueError, otherside_rightangle, 2, 0)
