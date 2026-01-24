import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(arc_length(10, 30), 31.4)
        self.assertAlmostEqual(arc_length(20, 90), 37.3)
        self.assertAlmostEqual(arc_length(30, 180), 52.6)

    def test_edge_cases(self):
        self.assertIsNone(arc_length(10, 360))
        self.assertIsNone(arc_length(20, 360))
        self.assertIsNone(arc_length(30, 360))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            arc_length("a", 30)
        with self.assertRaises(TypeError):
            arc_length(10, "a")
