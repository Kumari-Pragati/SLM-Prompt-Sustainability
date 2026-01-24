import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_polar_rect_zero(self):
        self.assertAlmostEqual(polar_rect(0, 0)[0].real, 0, delta=1e-6)
        self.assertAlmostEqual(polar_rect(0, 0)[0].imag, 0, delta=1e-6)
        self.assertAlmostEqual(polar_rect(0, 0)[1].real, 0, delta=1e-6)
        self.assertAlmostEqual(polar_rect(0, 0)[1].imag, 2 * cmath.pi, delta=1e-6)

    def test_polar_rect_positive(self):
        self.assertAlmostEqual(polar_rect(1, 0)[0].real, 1, delta=1e-6)
        self.assertAlmostEqual(polar_rect(1, 0)[0].imag, 0, delta=1e-6)
        self.assertAlmostEqual(polar_rect(1, 0)[1].real, cmath.pi / 2, delta=1e-6)
        self.assertAlmostEqual(polar_rect(1, 0)[1].imag, 0, delta=1e-6)

    def test_polar_rect_negative(self):
        self.assertAlmostEqual(polar_rect(-1, 0)[0].real, -1, delta=1e-6)
        self.assertAlmostEqual(polar_rect(-1, 0)[0].imag, 0, delta=1e-6)
        self.assertAlmostEqual(polar_rect(-1, 0)[1].real, -cmath.pi / 2, delta=1e-6)
        self.assertAlmostEqual(polar_rect(-1, 0)[1].imag, 0, delta=1e-6)

    def test_polar_rect_nonzero(self):
        self.assertAlmostEqual(polar_rect(1, 1)[0].real, 1.41421356237, delta=1e-6)
        self.assertAlmostEqual(polar_rect(1, 1)[0].imag, 0.785398163397, delta=1e-6)
        self.assertAlmostEqual(polar_rect(1, 1)[1].real, cmath.pi / 4, delta=1e-6)
        self.assertAlmostEqual(polar_rect(1, 1)[1].imag, 1.57079632679, delta=1e-6)
