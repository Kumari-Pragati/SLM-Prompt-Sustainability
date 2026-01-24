import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(arc_length(10, 90), 22/7)

    def test_boundary_case(self):
        self.assertIsNone(arc_length(10, 360))

    def test_edge_case(self):
        self.assertAlmostEqual(arc_length(10, 0), 0)
        self.assertAlmostEqual(arc_length(10, 359), 22/7 * 10 * 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            arc_length('10', 90)
        with self.assertRaises(TypeError):
            arc_length(10, '90')
        with self.assertRaises(TypeError):
            arc_length('10', '90')
        with self.assertRaises(ValueError):
            arc_length(10, -90)
        with self.assertRaises(ValueError):
            arc_length(10, 361)
