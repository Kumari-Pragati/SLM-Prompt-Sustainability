import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_typical_use_case(self):
        cn, cn1 = polar_rect(1, 2)
        self.assertIsInstance(cn, complex)
        self.assertIsInstance(cn1, complex)
        self.assertAlmostEqual(cn.real, 1)
        self.assertAlmostEqual(cn.imag, 2)
        self.assertAlmostEqual(cn1.real, 2)
        self.assertAlmostEqual(cn1.imag, 1)

    def test_zero_angle(self):
        cn, cn1 = polar_rect(0, 0)
        self.assertAlmostEqual(cn.real, 0)
        self.assertAlmostEqual(cn.imag, 0)
        self.assertAlmostEqual(cn1.real, 0)
        self.assertAlmostEqual(cn1.imag, 0)

    def test_pi_angle(self):
        cn, cn1 = polar_rect(1, 1)
        self.assertAlmostEqual(cn.real, 1)
        self.assertAlmostEqual(cn.imag, 1)
        self.assertAlmostEqual(cn1.real, 1)
        self.assertAlmostEqual(cn1.imag, 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 2)
