import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))

    def test_typical_case_2(self):
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))

    def test_typical_case_3(self):
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_boundary_condition(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_boundary_condition_2(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))

    def test_edge_case(self):
        self.assertEqual(rgb_to_hsv(128, 128, 128), (0, 0, 50))

    def test_edge_case_2(self):
        self.assertEqual(rgb_to_hsv(255, 128, 0), (30, 100, 100))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(-1, 0, 0)

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(256, 0, 0)
