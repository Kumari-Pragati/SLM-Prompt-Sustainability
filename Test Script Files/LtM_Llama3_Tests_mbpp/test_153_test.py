import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(parabola_vertex(1, 2, 3), ((-2/2, ((4*1*3)-(2**2))/(4*1))))

    def test_edge_cases(self):
        self.assertEqual(parabola_vertex(0, 0, 0), ((0, 0)))
        self.assertEqual(parabola_vertex(1, 0, 0), ((0, 0)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_vertex('a', 'b', 'c')

    def test_edge_case_negative_a(self):
        self.assertEqual(parabola_vertex(-1, 2, 3), ((-2/-2, ((4*(-1)*3)-(2**2))/((-2)*-1))))

    def test_edge_case_zero_a(self):
        self.assertEqual(parabola_vertex(0, 0, 0), ((0, 0)))

    def test_edge_case_zero_b(self):
        self.assertEqual(parabola_vertex(1, 0, 0), ((0, 0)))

    def test_edge_case_zero_c(self):
        self.assertEqual(parabola_vertex(1, 2, 0), ((-2/2, ((4*1*0)-(2**2))/(4*1))))
