import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_normal_case(self):
        self.assertTupleEqual(polar_rect(1, 1), (cmath.rect(1, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1, 1), (cmath.rect(-1, cmath.pi), cmath.rect(2, cmath.pi + cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 1), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))

    def test_edge_cases(self):
        self.assertTupleEqual(polar_rect(1e-10, 1e-10), (cmath.rect(1e-10, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1e10, 1e-10), (cmath.rect(-1e10, cmath.pi), cmath.rect(2, cmath.pi + cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 1e-10), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))

    def test_boundary_cases(self):
        self.assertTupleEqual(polar_rect(1, 0), (cmath.rect(1, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1, 0), (cmath.rect(-1, cmath.pi), cmath.rect(2, cmath.pi + cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 0), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))
