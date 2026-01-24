import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(arc_length(10, 90), 15.71, places=2)

    def test_boundary_condition(self):
        self.assertEqual(arc_length(10, 360), None)

    def test_edge_condition(self):
        self.assertAlmostEqual(arc_length(10, 1), 0.396, places=3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            arc_length("10", 90)
        with self.assertRaises(TypeError):
            arc_length(10, "90")
        with self.assertRaises(TypeError):
            arc_length("10", "90")
        with self.assertRaises(ValueError):
            arc_length(10, 361)
