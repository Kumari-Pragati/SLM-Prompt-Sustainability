import unittest
from mbpp_293_code import sqrt

def otherside_rightangle(w, h):
    s = sqrt((w * w) + (h * h))
    return s

class TestOthersideRightangle(unittest.TestCase):

    def test_otherside_rightangle_positive(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, 12), 13.0)
        self.assertAlmostEqual(otherside_rightangle(10, 20), 22.459425926506348)

    def test_otherside_rightangle_zero(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)

    def test_otherside_rightangle_negative(self):
        self.assertAlmostEqual(otherside_rightangle(-3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, -12), 13.0)
        self.assertAlmostEqual(otherside_rightangle(-10, -20), 22.459425926506348)
