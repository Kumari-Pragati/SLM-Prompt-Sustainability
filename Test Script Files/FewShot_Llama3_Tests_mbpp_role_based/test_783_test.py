import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):
    def test_valid_rgb_values(self):
        h, s, v = rgb_to_hsv(255, 0, 0)
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(s, 100)
        self.assertAlmostEqual(v, 100)

    def test_zero_rgb_values(self):
        h, s, v = rgb_to_hsv(0, 0, 0)
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(s, 0)
        self.assertAlmostEqual(v, 0)

    def test_max_rgb_values(self):
        h, s, v = rgb_to_hsv(255, 255, 255)
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(s, 0)
        self.assertAlmostEqual(v, 100)

    def test_min_rgb_values(self):
        h, s, v = rgb_to_hsv(0, 0, 0)
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(s, 0)
        self.assertAlmostEqual(v, 0)

    def test_invalid_rgb_values(self):
        with self.assertRaises(TypeError):
            rgb_to_hsv('a', 0, 0)
