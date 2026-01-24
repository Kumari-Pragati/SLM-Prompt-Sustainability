import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)
        self.assertAlmostEqual(otherside_rightangle(5, 12), 13.0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)
        self.assertAlmostEqual(otherside_rightangle(0, 1), 1.0)
        self.assertAlmostEqual(otherside_rightangle(1, 0), 1.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(otherside_rightangle(1, 1), math.sqrt(2))
        self.assertAlmostEqual(otherside_rightangle(1000, 1000), 1414.213562373095)

    def test_complex_cases(self):
        self.assertAlmostEqual(otherside_rightangle(3.5, 4.5), 5.830951894845301)
        self.assertAlmostEqual(otherside_rightangle(123456789, 987654321), 1.668104688778726e+09)
