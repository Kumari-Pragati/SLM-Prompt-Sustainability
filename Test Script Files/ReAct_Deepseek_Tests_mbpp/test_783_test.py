import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_edge_cases(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_explicitly_handled_error_cases(self):
        # Since the function already handles the case where r, g, b are 0,
        # we don't need to test for that.
        # We can test for cases where r, g, b are negative or greater than 255.
        self.assertEqual(rgb_to_hsv(-1, 0, 0), (0, 0, 0))
        self.assertEqual(rgb_to_hsv(256, 0, 0), (0, 0, 0))
