import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(polar_rect(1,2), (cmath.rect(1, 2), cmath.rect(2, cmath.pi)))

    def test_edge_cases(self):
        self.assertEqual(polar_rect(0,0), (cmath.rect(0, 0), cmath.rect(2, cmath.pi)))
        self.assertEqual(polar_rect(1,0), (cmath.rect(1, 0), cmath.rect(2, cmath.pi)))
        self.assertEqual(polar_rect(0,1), (cmath.rect(0, 1), cmath.rect(2, cmath.pi)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 2)
        with self.assertRaises(TypeError):
            polar_rect(1, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(polar_rect(-1,2), (cmath.rect(-1, 2), cmath.rect(2, cmath.pi)))
        self.assertEqual(polar_rect(1,-2), (cmath.rect(1, -2), cmath.rect(2, cmath.pi)))
