import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_vertex(self):
        self.assertEqual(parabola_vertex(1, 2, 3), (1, -1))
        self.assertEqual(parabola_vertex(2, 3, 4), (1, -2))
        self.assertEqual(parabola_vertex(3, 4, 5), (1, -3))

    def test_vertex_type(self):
        self.assertIsInstance(parabola_vertex(1, 2, 3), tuple)
