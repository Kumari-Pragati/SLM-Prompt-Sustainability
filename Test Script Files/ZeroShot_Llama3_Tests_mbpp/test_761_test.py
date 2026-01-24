import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_arc_length_valid_input(self):
        self.assertAlmostEqual(arc_length(10, 90), 31.416666666666668, places=8)

    def test_arc_length_invalid_input(self):
        self.assertIsNone(arc_length(10, 400))

    def test_arc_length_zero_angle(self):
        self.assertIsNone(arc_length(10, 0))

    def test_arc_length_zero_radius(self):
        self.assertIsNone(arc_length(0, 90))

    def test_arc_length_invalid_radius(self):
        with self.assertRaises(TypeError):
            arc_length('a', 90)

    def test_arc_length_invalid_angle(self):
        with self.assertRaises(TypeError):
            arc_length(10, 'b')
