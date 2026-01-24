import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertListEqual(rgb_to_hsv(255, 0, 0), [0, 100, 100])
        self.assertListEqual(rgb_to_hsv(0, 255, 0), [120, 100, 100])
        self.assertListEqual(rgb_to_hsv(0, 0, 255), [240, 100, 100])
        self.assertListEqual(rgb_to_hsv(255, 255, 255), [0, 0, 100])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(rgb_to_hsv(0, 0, 0), [0, 0, 0])
        self.assertListEqual(rgb_to_hsv(255, 255, 255), [0, 0, 100])
        self.assertListEqual(rgb_to_hsv(1, 1, 1), [0, 0, 100])
        self.assertListEqual(rgb_to_hsv(-1, -1, -1), [0, 0, 0])
        self.assertListEqual(rgb_to_hsv(256, 0, 0), [0, 0, 100])
        self.assertListEqual(rgb_to_hsv(0, 256, 0), [120, 0, 100])
        self.assertListEqual(rgb_to_hsv(0, 0, 256), [240, 0, 100])

    def test_special_cases(self):
        self.assertListEqual(rgb_to_hsv(255, 255, 0), [60, 100, 100])
        self.assertListEqual(rgb_to_hsv(255, 0, 255), [240, 100, 100])
        self.assertListEqual(rgb_to_hsv(0, 255, 255), [120, 100, 100])
        self.assertListEqual(rgb_to_hsv(255, 255, 255), [0, 0, 100])
