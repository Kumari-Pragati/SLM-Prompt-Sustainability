import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_vertex(1, -3, 2), (1.5, 1.25))

    def test_boundary_case(self):
        self.assertEqual(parabola_vertex(1, 0, 0), (0, 0))

    def test_edge_case(self):
        self.assertEqual(parabola_vertex(1, -2, 1), (1, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_vertex('a', 'b', 'c')
