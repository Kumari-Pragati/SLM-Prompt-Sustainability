import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_positive_angle(self):
        self.assertAlmostEqual(arc_length(10, 90), 28.274333882308138)
        self.assertAlmostEqual(arc_length(10, 180), 56.54822574358935)
        self.assertAlmostEqual(arc_length(10, 270), 56.54822574358935)

    def test_zero_angle(self):
        self.assertEqual(arc_length(10, 0), 0)

    def test_negative_angle(self):
        self.assertEqual(arc_length(10, -90), None)
        self.assertEqual(arc_length(10, -180), None)
        self.assertEqual(arc_length(10, -270), None)
        self.assertEqual(arc_length(10, -361), None)

    def test_zero_distance(self):
        self.assertEqual(arc_length(0, 90), 0)
        self.assertEqual(arc_length(0, 180), 0)
        self.assertEqual(arc_length(0, 270), 0)
        self.assertEqual(arc_length(0, 360), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, arc_length, 'str', 90)
        self.assertRaises(TypeError, arc_length, 10, 'str')
        self.assertRaises(ValueError, arc_length, -10, 90)
        self.assertRaises(ValueError, arc_length, 10, 361)
