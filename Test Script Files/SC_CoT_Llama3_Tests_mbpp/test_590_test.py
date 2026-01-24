import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(polar_rect(1, 2), (cmath.rect(1, 2), cmath.rect(2, cmath.pi)))

    def test_zero_angle(self):
        self.assertEqual(polar_rect(1, 0), (cmath.rect(1, 0), cmath.rect(2, cmath.pi)))

    def test_negative_angle(self):
        self.assertEqual(polar_rect(1, -cmath.pi), (cmath.rect(1, -cmath.pi), cmath.rect(2, cmath.pi)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 2)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            polar_rect(1, 'b')

    def test_edge_case(self):
        self.assertEqual(polar_rect(0, 0), (cmath.rect(0, 0), cmath.rect(2, cmath.pi)))

    def test_edge_case2(self):
        self.assertEqual(polar_rect(float('inf'), 0), (cmath.rect(float('inf'), 0), cmath.rect(2, cmath.pi)))
