import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)

    def test_zero_input(self):
        with self.assertRaises(ZeroDivisionError):
            otherside_rightangle(0, 4)

    def test_negative_input(self):
        self.assertAlmostEqual(otherside_rightangle(-3, 4), 5.0)

    def test_zero_input_again(self):
        with self.assertRaises(ZeroDivisionError):
            otherside_rightangle(4, 0)

    def test_edge_case(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)

    def test_large_input(self):
        self.assertAlmostEqual(otherside_rightangle(100, 200), 223.6)
