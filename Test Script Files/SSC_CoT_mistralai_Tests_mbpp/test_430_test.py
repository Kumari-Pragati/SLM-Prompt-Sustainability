import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(parabola_directrix(1, 2, 5), 13)
        self.assertEqual(parabola_directrix(-1, -2, -5), -13)
        self.assertEqual(parabola_directrix(2, 3, 10), -2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(parabola_directrix(0, 0, 1), 3)
        self.assertEqual(parabola_directrix(0, 0, -1), -3)
        self.assertEqual(parabola_directrix(1, 0, 1), 3)
        self.assertEqual(parabola_directrix(1, 0, -1), -3)
        self.assertEqual(parabola_directrix(1, 1, 1), 0)
        self.assertEqual(parabola_directrix(1, 1, -1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, parabola_directrix, 0, 0, 0)
        self.assertRaises(ValueError, parabola_directrix, 0, 'not_a_number', 1)
        self.assertRaises(ValueError, parabola_directrix, 'not_a_number', 0, 1)
