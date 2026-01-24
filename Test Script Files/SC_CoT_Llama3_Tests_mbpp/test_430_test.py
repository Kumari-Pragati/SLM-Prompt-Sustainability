import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -2)

    def test_edge_cases(self):
        self.assertEqual(parabola_directrix(1, 0, 1), -1)
        self.assertEqual(parabola_directrix(1, 0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(parabola_directrix(1, 1, 1), -1)
        self.assertEqual(parabola_directrix(1, -1, 1), 1)

    def test_special_cases(self):
        self.assertEqual(parabola_directrix(1, 2, 0), 0)
        self.assertEqual(parabola_directrix(1, -2, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_directxis(1, 2, 'c')
