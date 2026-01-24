import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_positive_angle(self):
        self.assertTupleEqual(polar_rect(1, 1), (cmath.polar(1+0j), cmath.rect(2, 0)))
        self.assertTupleEqual(polar_rect(-1, 1), (cmath.polar(-1+0j), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 1), (cmath.polar(0+0j), cmath.rect(2, cmath.pi/2)))

    def test_zero_arguments(self):
        with self.assertRaises(ValueError):
            polar_rect(0, 0)

    def test_negative_real(self):
        self.assertTupleEqual(polar_rect(-1, -1), (cmath.polar(-1-0j), cmath.rect(2, cmath.pi)))

    def test_edge_cases(self):
        self.assertTupleEqual(polar_rect(0, 0), (cmath.polar(0+0j), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(1, 0), (cmath.polar(1+0j), cmath.rect(2, cmath.pi/2)))
        self.assertTupleEqual(polar_rect(0, 1), (cmath.polar(0+0j), cmath.rect(2, cmath.pi/2)))
