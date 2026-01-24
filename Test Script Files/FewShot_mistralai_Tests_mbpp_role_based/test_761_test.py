import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_positive_degrees_and_radius(self):
        self.assertAlmostEqual(arc_length(1, 90), 2.0 * 22 / 7)

    def test_zero_degrees_and_radius(self):
        self.assertEqual(arc_length(1, 0), 0)

    def test_negative_degrees_and_radius(self):
        self.assertIsNone(arc_length(1, -180))

    def test_large_degrees_and_radius(self):
        self.assertIsNone(arc_length(1, 361))

    def test_zero_radius_and_degrees(self):
        self.assertIsNone(arc_length(0, 90))
