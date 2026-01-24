import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(otherside_rightangle(3, 4), 5)
        self.assertEqual(otherside_rightangle(4, 3), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(otherside_rightangle(0, 0), 0)
        self.assertEqual(otherside_rightangle(1, 1), 2)
        self.assertEqual(otherside_rightangle(math.inf, math.inf), math.inf)
        self.assertEqual(otherside_rightangle(-1, -1), 2)
        self.assertEqual(otherside_rightangle(-1, math.inf), math.inf)
        self.assertEqual(otherside_rightangle(math.inf, -1), math.inf)

    def test_negative_input(self):
        self.assertRaises(ValueError, otherside_rightangle, -3, 4)
        self.assertRaises(ValueError, otherside_rightangle, 3, -4)
