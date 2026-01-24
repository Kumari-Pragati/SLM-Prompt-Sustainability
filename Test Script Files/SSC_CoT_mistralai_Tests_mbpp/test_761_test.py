import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(arc_length(10, 90), 28.274333882308138)
        self.assertEqual(arc_length(2.5, 180), 15.707963267948966)
        self.assertEqual(arc_length(3, 360), 282.74333882308138)

    def test_edge_and_boundary_conditions(self):
        self.assertIsNone(arc_length(1, 361))
        self.assertIsNone(arc_length(0, 360))
        self.assertIsNone(arc_length(-1, 360))
        self.assertIsNone(arc_length(1, 0))
        self.assertIsNone(arc_length(1, -360))
        self.assertIsNone(arc_length(0, 0))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, arc_length, -1, 360)
        self.assertRaises(ValueError, arc_length, 0, 'not_a_number')
        self.assertRaises(ValueError, arc_length, 'not_a_number', 360)
