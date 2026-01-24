import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(polar_rect(1, 2), (cmath.rect(1, 2), cmath.rect(2, cmath.pi)))

    def test_zero_input(self):
        self.assertEqual(polar_rect(0, 0), (cmath.rect(0, 0), cmath.rect(2, cmath.pi)))

    def test_negative_input(self):
        self.assertEqual(polar_rect(-1, -2), (cmath.rect(-1, -2), cmath.rect(2, cmath.pi)))

    def test_edge_case_pi(self):
        self.assertEqual(polar_rect(1, cmath.pi), (cmath.rect(1, cmath.pi), cmath.rect(2, cmath.pi)))

    def test_edge_case_negative_pi(self):
        self.assertEqual(polar_rect(1, -cmath.pi), (cmath.rect(1, -cmath.pi), cmath.rect(2, cmath.pi)))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 2)
