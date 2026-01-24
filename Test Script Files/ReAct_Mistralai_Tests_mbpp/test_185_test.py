import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_positive_numbers(self):
        """Test parabola_focus with positive numbers"""
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (0.5, 2.5))
        self.assertAlmostEqual(parabola_focus(2, 4, 4), (0, 1))
        self.assertAlmostEqual(parabola_focus(3, 6, 9), (-0.5, 3))

    def test_zero_numbers(self):
        """Test parabola_focus with zero numbers"""
        self.assertAlmostEqual(parabola_focus(0, 0, 0), (None, None))
        self.assertAlmostEqual(parabola_focus(0, 0, 1), (None, None))
        self.assertAlmostEqual(parabola_focus(1, 0, 0), (None, None))

    def test_negative_numbers(self):
        """Test parabola_focus with negative numbers"""
        self.assertAlmostEqual(parabola_focus(-1, -2, -3), (0.5, -2.5))
        self.assertAlmostEqual(parabola_focus(-2, -4, -4), (0, -1))
        self.assertAlmostEqual(parabola_focus(-3, -6, -9), (-0.5, -3))

    def test_invalid_input(self):
        """Test parabola_focus with invalid inputs"""
        self.assertRaises(ValueError, parabola_focus, 0, 0, 0)
        self.assertRaises(ValueError, parabola_focus, 1, 0, 0)
        self.assertRaises(ValueError, parabola_focus, 0, 1, 0)
