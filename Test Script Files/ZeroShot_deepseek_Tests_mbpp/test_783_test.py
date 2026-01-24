import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_black(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_white(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))

    def test_red(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))

    def test_green(self):
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))

    def test_blue(self):
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_yellow(self):
        self.assertEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))

    def test_cyan(self):
        self.assertEqual(rgb_to_hsv(0, 255, 255), (180, 100, 100))

    def test_magenta(self):
        self.assertEqual(rgb_to_hsv(255, 0, 255), (300, 100, 100))

    def test_gray(self):
        self.assertEqual(rgb_to_hsv(128, 128, 128), (0, 0, 50))

    def test_random(self):
        self.assertEqual(rgb_to_hsv(100, 200, 50), (33.333333333333336, 100.0, 88.23529411764706))
