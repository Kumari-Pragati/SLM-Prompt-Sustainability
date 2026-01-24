import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(otherside_rightangle(3, 4), 5.0)

    def test_typical_case_2(self):
        self.assertAlmostEqual(otherside_rightangle(5, 12), 13.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(otherside_rightangle(0, 0), 0.0)
        self.assertAlmostEqual(otherside_rightangle(0, 1), 1.0)
        self.assertAlmostEqual(otherside_rightangle(1, 0), 1.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(otherside_rightangle(1, 1), math.sqrt(2))
        self.assertAlmostEqual(otherside_rightangle(1, -1), math.sqrt(2))
        self.assertAlmostEqual(otherside_rightangle(-1, 1), math.sqrt(2))
        self.assertAlmostEqual(otherside_rightangle(-1, -1), math.sqrt(2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            otherside_rightangle("a", 1)
        with self.assertRaises(TypeError):
            otherside_rightangle(1, "a")
        with self.assertRaises(TypeError):
            otherside_rightangle("a", "b")
