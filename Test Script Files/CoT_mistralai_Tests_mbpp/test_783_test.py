import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertAlmostEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertAlmostEqual(rgb_to_hsv(128, 0, 128), (300, 50, 50))

    def test_edge_cases(self):
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 255), (120, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 0, 255), (240, 100, 100))

    def test_boundary_conditions(self):
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 254), (0, 0, 99.99))
        self.assertAlmostEqual(rgb_to_hsv(254, 0, 0), (0, 99.99, 100))
        self.assertAlmostEqual(rgb_to_hsv(255, 254, 0), (60, 99.99, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 254), (120, 99.99, 100))
        self.assertAlmostEqual(rgb_to_hsv(254, 255, 0), (240, 99.99, 100))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, rgb_to_hsv, -1, 0, 0)
        self.assertRaises(ValueError, rgb_to_hsv, 256, 0, 0)
        self.assertRaises(ValueError, rgb_to_hsv, 0, -1, 0)
        self.assertRaises(ValueError, rgb_to_hsv, 0, 256, 0)
        self.assertRaises(ValueError, rgb_to_hsv, 0, 0, -1)
