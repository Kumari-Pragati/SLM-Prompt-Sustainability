import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))

    def test_edge_case(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_edge_case2(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))

    def test_edge_case3(self):
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))

    def test_edge_case4(self):
        self.assertEqual(rgb_to_hsv(255, 0, 255), (240, 100, 100))

    def test_edge_case5(self):
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_edge_case6(self):
        self.assertEqual(rgb_to_hsv(255, 255, 0), (60, 100, 100))

    def test_edge_case7(self):
        self.assertEqual(rgb_to_hsv(0, 255, 255), (60, 100, 100))

    def test_edge_case8(self):
        self.assertEqual(rgb_to_hsv(255, 0, 255), (240, 100, 100))

    def test_edge_case9(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_edge_case10(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
