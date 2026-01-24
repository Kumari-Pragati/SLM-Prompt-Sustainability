import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(128, 128, 128), (0, 0, 50))
        self.assertEqual(rgb_to_hsv(192, 192, 192), (0, 0, 75))

    def test_invalid_inputs(self):
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
