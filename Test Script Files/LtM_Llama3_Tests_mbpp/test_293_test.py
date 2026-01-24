import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(otherside_rightangle(3, 4), 5.0)
        self.assertEqual(otherside_rightangle(5, 12), 13.0)
        self.assertEqual(otherside_rightangle(7, 24), 25.0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(otherside_rightangle(0, 0), 0.0)
        self.assertEqual(otherside_rightangle(0, 10), 10.0)
        self.assertEqual(otherside_rightangle(10, 0), 10.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            otherside_rightangle('a', 4)
        with self.assertRaises(TypeError):
            otherside_rightangle(3, 'b')
