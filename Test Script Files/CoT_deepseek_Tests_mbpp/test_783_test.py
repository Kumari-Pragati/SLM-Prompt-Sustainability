import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_edge_cases(self):
        self.assertAlmostEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rgb_to_hsv("255", 0, 0)
        with self.assertRaises(TypeError):
            rgb_to_hsv(255, "0", 0)
        with self.assertRaises(TypeError):
            rgb_to_hsv(255, 0, "0")
        with self.assertRaises(ValueError):
            rgb_to_hsv(-1, 0, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(256, 0, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, -1, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 256, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 0, -1)
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 0, 256)
