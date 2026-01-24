import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)

    def test_zero_input(self):
        self.assertEqual(otherside_rightangle(0, 0), 0)
        self.assertEqual(otherside_rightangle(0, 4), 4)
        self.assertEqual(otherside_rightangle(3, 0), 3)

    def test_negative_input(self):
        self.assertAlmostEqual(otherside_rightangle(-3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(3, -4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(-3, -4), 5.0)

    def test_large_input(self):
        self.assertAlmostEqual(otherside_rightangle(10000, 10000), 14142.13562373095)
