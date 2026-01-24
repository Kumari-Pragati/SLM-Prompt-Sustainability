import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 0), (60, 0, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 255), (240, 0, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 255), (300, 0, 100))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 255), (300, 0, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 255), (300, 0, 100))
        self.assertEqual(rgb_to_hsv(1, 1, 1), (0, 0, 100.01))
