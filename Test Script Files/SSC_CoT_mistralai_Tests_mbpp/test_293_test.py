import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightAngle(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(otherside_rightangle(3, 4), math.sqrt(25 + 16))

    def test_edge_input(self):
        self.assertEqual(otherside_rightangle(0, 4), 4)
        self.assertEqual(otherside_rightangle(4, 0), 4)
        self.assertEqual(otherside_rightangle(0, 0), 0)

    def test_negative_input(self):
        self.assertRaises(ValueError, otherside_rightangle, -3, 4)
        self.assertRaises(ValueError, otherside_rightangle, 3, -4)

    def test_float_input(self):
        self.assertAlmostEqual(otherside_rightangle(3.5, 4.0), math.sqrt(25 + 16))
        self.assertAlmostEqual(otherside_rightangle(0.0, 4.0), 4)
