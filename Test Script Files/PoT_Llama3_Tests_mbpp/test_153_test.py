import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, 3), (-1, -1))

    def test_edge_case_a_zero(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, 2, 3)

    def test_edge_case_b_zero(self):
        self.assertAlmostEqual(parabola_vertex(1, 0, 3), (0, 3))

    def test_edge_case_c_zero(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, 0), (-2, 0))

    def test_edge_case_a_negative(self):
        self.assertAlmostEqual(parabola_vertex(-1, 2, 3), (1, 1))

    def test_edge_case_b_negative(self):
        self.assertAlmostEqual(parabola_vertex(1, -2, 3), (1, 3))

    def test_edge_case_c_negative(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, -3), (-2, -3))

    def test_edge_case_a_zero_and_b_zero(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, 0, 3)

    def test_edge_case_a_zero_and_c_zero(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, 2, 0)

    def test_edge_case_b_zero_and_c_zero(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(1, 0, 0)
