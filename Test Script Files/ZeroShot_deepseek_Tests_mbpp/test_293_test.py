import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_otherside_rightangle(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, 12), 13.0)
        self.assertAlmostEqual(otherside_rightangle(8, 15), 17.0)
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)
        self.assertAlmostEqual(otherside_rightangle(7, 0), 7.0)
        self.assertAlmostEqual(otherside_rightangle(0, 8), 8.0)
        self.assertAlmostEqual(otherside_rightangle(3.5, 4.5), 6.0827625303)
