import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(parabola_vertex(1, 2, 3), ((-2.0/2), ((4*1*3)-(2**2))/(4*1)))

    def test_edge_cases(self):
        self.assertEqual(parabola_vertex(0, 0, 0), (0, 0))
        self.assertEqual(parabola_vertex(1, 0, 0), (0, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_vertex('a', 'b', 'c')
        with self.assertRaises(TypeError):
            parabola_vertex(1, 'b', 'c')
        with self.assertRaises(TypeError):
            parabola_vertex(1, 2, 'c')

    def test_boundary_conditions(self):
        self.assertEqual(parabola_vertex(1, 0, 0), (0, 0))
        self.assertEqual(parabola_vertex(1, 0, 1), (0, 1))
