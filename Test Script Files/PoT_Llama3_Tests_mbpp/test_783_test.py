import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))

    def test_edge_case(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))

    def test_boundary_case(self):
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 255), (240, 100, 100))

    def test_corner_case(self):
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rgb_to_hsv('a', 0, 0)
        with self.assertRaises(TypeError):
            rgb_to_hsv(0, 'b', 0)
        with self.assertRaises(TypeError):
            rgb_to_hsv(0, 0, 'c')
