import unittest
from mbpp_590_code import polar_rect
import cmath

class TestPolarRect(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(polar_rect(1, 1), ((1.4142135623730951, 0.7853981633974483), (1+0j)))

    def test_boundary_conditions(self):
        self.assertEqual(polar_rect(0, 0), ((0, 0), (0+0j)))
        self.assertEqual(polar_rect(1, cmath.pi), ((1.2732395447351627e-16, 1.5707963267948966), (6.123233995736766e-17+1j)))

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            polar_rect("1", 1)
        with self.assertRaises(TypeError):
            polar_rect(1, "1")
