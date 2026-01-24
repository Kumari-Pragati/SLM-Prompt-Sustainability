import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)

    def test_edge_case(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(otherside_rightangle(1, 1), 1.4142135623730951)
        self.assertAlmostEqual(otherside_rightangle(math.sqrt(2), math.sqrt(2)), 2.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            otherside_rightangle("3", 4)
        with self.assertRaises(TypeError):
            otherside_rightangle(3, "4")
        with self.assertRaises(TypeError):
            otherside_rightangle("3", "4")
