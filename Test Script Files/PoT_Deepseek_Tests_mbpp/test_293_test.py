import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, 12), 13.0)
        self.assertAlmostEqual(otherside_rightangle(8, 15), 17.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)
        self.assertAlmostEqual(otherside_rightangle(0, 10), 10.0)
        self.assertAlmostEqual(otherside_rightangle(10, 0), 10.0)

    def test_boundary_cases(self):
        self.assertAlmostEqual(otherside_rightangle(1, 1), 1.4142135623730951)
        self.assertAlmostEqual(otherside_rightangle(1000, 1000), 1414.213562373095)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            otherside_rightangle("3", 4)
        with self.assertRaises(TypeError):
            otherside_rightangle(3, "4")
        with self.assertRaises(TypeError):
            otherside_rightangle("3", "4")
