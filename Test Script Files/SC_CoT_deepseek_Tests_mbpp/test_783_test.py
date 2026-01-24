import unittest
from mbpp_783_code import rgb_to_hsv

class TestRGBToHSV(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 100, 100))

    def test_typical_case_2(self):
        self.assertEqual(rgb_to_hsv(0, 255, 0), (120, 100, 100))

    def test_typical_case_3(self):
        self.assertEqual(rgb_to_hsv(0, 0, 255), (240, 100, 100))

    def test_boundary_case(self):
        self.assertEqual(rgb_to_hsv(0, 0, 0), (0, 0, 0))

    def test_boundary_case_2(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100))

    def test_edge_case(self):
        self.assertEqual(rgb_to_hsv(1, 1, 1), (0, 0, 0.00392156862745098))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rgb_to_hsv("red", 0, 0)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            rgb_to_hsv(255, "green", 0)

    def test_invalid_input_3(self):
        with self.assertRaises(TypeError):
            rgb_to_hsv(255, 0, "blue")

    def test_invalid_input_4(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(-1, 0, 0)

    def test_invalid_input_5(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(256, 0, 0)

    def test_invalid_input_6(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, -1, 0)

    def test_invalid_input_7(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 256, 0)

    def test_invalid_input_8(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 0, -1)

    def test_invalid_input_9(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 0, 256)
