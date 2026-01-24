import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5)
        self.assertAlmostEqual(otherside_rightangle(4, 3), 5)

    def test_zero(self):
        self.assertEqual(otherside_rightangle(0, 0), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(otherside_rightangle(-3, 4), 5)
        self.assertAlmostEqual(otherside_rightangle(3, -4), 5)

    def test_one_zero(self):
        self.assertEqual(otherside_rightangle(0, 3), 3)
        self.assertEqual(otherside_rightangle(3, 0), 3)

    def test_negative_one_zero(self):
        self.assertEqual(otherside_rightangle(0, -3), 3)
        self.assertEqual(otherside_rightangle(-3, 0), 3)
