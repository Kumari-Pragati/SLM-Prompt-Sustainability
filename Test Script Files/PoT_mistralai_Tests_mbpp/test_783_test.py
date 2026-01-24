import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 255), (300, 100, 100))

    def test_edge_and_boundary_cases(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(1, 1, 1), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 255.001), (240, 100, 100.001))
        self.assertEqual(rgb_to_hsv(255, 0, 255.001), (300, 100, 100.001))
        self.assertEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
