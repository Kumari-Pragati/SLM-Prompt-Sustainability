import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(arc_length(10, 90), 15.708, places=3)

    def test_full_circle(self):
        self.assertIsNone(arc_length(10, 360))

    def test_zero_angle(self):
        self.assertEqual(arc_length(10, 0), 0)

    def test_negative_angle(self):
        self.assertIsNone(arc_length(10, -10))

    def test_large_angle(self):
        self.assertIsNone(arc_length(10, 400))

    def test_zero_diameter(self):
        self.assertEqual(arc_length(0, 90), 0)

    def test_negative_diameter(self):
        self.assertIsNone(arc_length(-10, 90))
