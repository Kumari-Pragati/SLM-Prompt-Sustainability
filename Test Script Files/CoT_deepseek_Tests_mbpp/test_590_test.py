import unittest
from mbpp_590_code import polar_rect
import cmath

class TestPolarRect(unittest.TestCase):

    def test_typical_case(self):
        self.assertTupleEqual(polar_rect(1, 1), ((1.4142135623730951, 0.7853981633974483), (1+0j)))

    def test_zero_input(self):
        self.assertTupleEqual(polar_rect(0, 0), ((0, 0), (0+0j)))

    def test_negative_input(self):
        self.assertTupleEqual(polar_rect(-1, -1), ((1.4142135623730951, 2.356194490192345), (-1-1j)))

    def test_large_input(self):
        self.assertTupleEqual(polar_rect(1000, 1000), ((1414.213562373095, 1.1071487177940904), (1000+1000j)))

    def test_pi_input(self):
        self.assertTupleEqual(polar_rect(cmath.cos(cmath.pi), cmath.sin(cmath.pi)), ((1.2246467991503283e-16, 1.5707963267948966), (6.123233995736766e-17-1j)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 'b')
