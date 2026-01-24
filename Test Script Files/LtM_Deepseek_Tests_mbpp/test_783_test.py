import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_edge_conditions(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_complex_cases(self):
        self.assertEqual(rgb_to_hsv(128, 128, 128), (0, 0, 50))
        self.assertEqual(rgb_to_hsv(192, 192, 192), (0, 0, 75))
        self.assertEqual(rgb_to_hsv(255, 128, 0), (30, 100, 100))
        self.assertEqual(rgb_to_hsv(128, 0, 255), (210, 100, 50))
        self.assertEqual(rgb_to_hsv(0, 255, 128), (90, 100, 50))
