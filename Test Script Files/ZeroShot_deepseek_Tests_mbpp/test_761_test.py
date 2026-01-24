import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_arc_length_with_valid_input(self):
        self.assertAlmostEqual(arc_length(10, 90), 3.141592653589793, places=5)
        self.assertAlmostEqual(arc_length(10, 180), 6.283185307179586, places=5)
        self.assertAlmostEqual(arc_length(10, 360), 12.566370614359172, places=5)

    def test_arc_length_with_invalid_input(self):
        self.assertIsNone(arc_length(10, 361))
        self.assertIsNone(arc_length(-10, 90))
        self.assertIsNone(arc_length(10, -90))
