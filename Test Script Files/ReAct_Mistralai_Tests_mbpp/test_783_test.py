import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_valid_colors(self):
        # Typical cases
        self.assertAlmostEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 255), (240, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 127, 0), (60, 75, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 0, 127), (240, 75, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 127, 255), (120, 75, 100))
        self.assertAlmostEqual(rgb_to_hsv(127, 0, 255), (240, 75, 100))
        self.assertAlmostEqual(rgb_to_hsv(127, 127, 0), (60, 50, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 127, 127), (240, 50, 100))
        self.assertAlmostEqual(rgb_to_hsv(127, 0, 127), (120, 50, 100))
        self.assertAlmostEqual(rgb_to_hsv(127, 127, 0), (60, 50, 100))

    def test_edge_cases(self):
        # Edge cases
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertAlmostEqual(rgb_to_hsv(1, 1, 1), (0, 0, 100.01))  # Check for slight rounding error
        self.assertAlmostEqual(rgb_to_hsv(-1, -1, -1), (0, 0, 0))
        self.assertAlmostEqual(rgb_to_hsv(256, 0, 0), (0, 0, 100))  # Check for invalid input
        self.assertAlmostEqual(rgb_to_hsv(0, 256, 0), (0, 0, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 256), (0, 0, 100))
