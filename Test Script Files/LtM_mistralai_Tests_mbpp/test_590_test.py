import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_simple(self):
        self.assertTupleEqual(polar_rect(1, 0), (cmath.rect(1, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(0, 1), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))

    def test_edge_cases(self):
        self.assertTupleEqual(polar_rect(-1, 0), (cmath.rect(-1, 0), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(0, -1), (cmath.rect(0, cmath.pi/2), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(1, 1), (cmath.rect(1.4142135623730951, cmath.pi/4), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1, -1), (cmath.rect(1.4142135623730951, cmath.pi/4), cmath.rect(2, cmath.pi)))

    def test_complex(self):
        self.assertTupleEqual(polar_rect(1, 2), (cmath.rect(1.7320508075688772, cmath.atan(2)), cmath.rect(2, cmath.pi)))
        self.assertTupleEqual(polar_rect(-1, -2), (cmath.rect(1.7320508075688772, cmath.atan(2)), cmath.rect(2, cmath.pi)))
