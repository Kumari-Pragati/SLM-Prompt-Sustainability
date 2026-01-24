import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -13)

    def test_boundary_case(self):
        self.assertEqual(parabola_directrix(0, 0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(parabola_directrix(1, 0, 0), -4)
        self.assertEqual(parabola_directrix(1, 0, 1), -5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 2, 'c')
