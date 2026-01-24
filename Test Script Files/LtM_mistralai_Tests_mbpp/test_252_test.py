import unittest
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):

    def test_simple_positive(self):
        self.assertAlmostEqual(convert(1), cmath.rect(1, 0))

    def test_simple_negative(self):
        self.assertAlmostEqual(convert(-1), cmath.rect(-1, 0))

    def test_simple_complex(self):
        self.assertAlmostEqual(convert(complex(1, 1)), cmath.rect(1.0050247580136719, 1.5707963267948966))

    def test_edge_zero(self):
        self.assertAlmostEqual(convert(0), cmath.rect(0, 0))

    def test_edge_pi(self):
        self.assertAlmostEqual(convert(1j), cmath.rect(1, cmath.pi/2))

    def test_edge_pi_negative(self):
        self.assertAlmostEqual(convert(-1j), cmath.rect(1, -cmath.pi/2))

    def test_edge_infinity(self):
        self.assertAlmostEqual(convert(float('inf')), cmath.rect(float('inf'), cmath.pi/2))

    def test_edge_negative_infinity(self):
        self.assertAlmostEqual(convert(-float('inf')), cmath.rect(-float('inf'), -cmath.pi/2))
