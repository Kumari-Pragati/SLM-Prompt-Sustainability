import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(polar_rect(1, 1), ((1.4142135623730951, 0.7853981633974483), (1+0j)))
        self.assertEqual(polar_rect(-1, -1), ((1.4142135623730951, -2.356194490192345), (-1-1j)))

    def test_edge_cases(self):
        self.assertEqual(polar_rect(0, 0), ((0, 0), 0j))
        self.assertEqual(polar_rect(1, 0), ((1, 0), 1+0j))
        self.assertEqual(polar_rect(0, 1), ((1.5707963267948966, 1.5707963267948966), 0+1j))

    def test_boundary_conditions(self):
        self.assertEqual(polar_rect(1, cmath.pi), ((1, cmath.pi), 1j))
        self.assertEqual(polar_rect(cmath.pi, 1), ((1.5707963267948966, 1.0000000000000002), 1j))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            polar_rect("1", 1)
        with self.assertRaises(TypeError):
            polar_rect(1, "1")
