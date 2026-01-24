import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTupleEqual(polar_rect(1, 0), (cmath.rect(1, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 1), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1, 0), (cmath.rect(-1, cmath.pi), cmath.rect(2, 3*cmath.pi)))
        self.assertTupleEqual(polar_rect(0, -1), (cmath.rect(0, cmath.pi/2 + cmath.pi), cmath.rect(2, 2*cmath.pi)))

    def test_edge_and_boundary_cases(self):
        self.assertTupleEqual(polar_rect(1e-8, 0), (cmath.rect(1e-8, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 1e-8), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1e-8, 0), (cmath.rect(-1e-8, cmath.pi), cmath.rect(2, 3*cmath.pi)))
        self.assertTupleEqual(polar_rect(0, -1e-8), (cmath.rect(0, cmath.pi/2 + cmath.pi), cmath.rect(2, 2*cmath.pi)))
        self.assertTupleEqual(polar_rect(1, 1), (cmath.rect(1, cmath.atan2(1, 1)), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1, -1), (cmath.rect(-1, cmath.atan2(-1, -1)), cmath.rect(2, 3*cmath.pi)))
        self.assertTupleEqual(polar_rect(1, -1), (cmath.rect(1, cmath.atan2(1, -1)), cmath.rect(2, cmath.pi + cmath.pi/2)))
        self.assertTupleEqual(polar_rect(-1, 1), (cmath.rect(-1, cmath.atan2(-1, 1)), cmath.rect(2, cmath.pi + cmath.pi/2 + cmath.pi)))
