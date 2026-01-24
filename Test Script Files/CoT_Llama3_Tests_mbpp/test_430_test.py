import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -5)

    def test_edge_cases(self):
        self.assertEqual(parabola_directrix(0, 0, 0), 0)
        self.assertEqual(parabola_directrix(1, 0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 'b', 'c')

    def test_boundary_conditions(self):
        self.assertEqual(parabola_directrix(1, 0, 1), 0)
        self.assertEqual(parabola_directrix(1, 0, -1), 0)
