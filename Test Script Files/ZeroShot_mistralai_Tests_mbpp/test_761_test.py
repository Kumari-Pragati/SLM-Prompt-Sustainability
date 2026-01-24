import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_arc_length_positive_values(self):
        self.assertAlmostEqual(arc_length(10, 90), 28.274333882308138)
        self.assertAlmostEqual(arc_length(5, 180), 314.1592653589793)
        self.assertAlmostEqual(arc_length(2, 360), 628.3185307179586)

    def test_arc_length_zero_degrees(self):
        self.assertEqual(arc_length(10, 0), 0)

    def test_arc_length_negative_degrees(self):
        self.assertAlmostEqual(arc_length(10, -90), -28.274333882308138)
        self.assertAlmostEqual(arc_length(5, -180), -314.1592653589793)
        self.assertAlmostEqual(arc_length(2, -360), -628.3185307179586)

    def test_arc_length_greater_than_360_degrees(self):
        self.assertIsNone(arc_length(10, 400))
        self.assertIsNone(arc_length(5, 720))
        self.assertIsNone(arc_length(2, 1080))
