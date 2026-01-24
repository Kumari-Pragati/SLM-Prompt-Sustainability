import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)

    def test_zero_input(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)

    def test_edge_case(self):
        self.assertAlmostEqual(otherside_rightangle(100, 100), 141.4213562373095)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            otherside_rightangle(-1, 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            otherside_rightangle('a', 2)
