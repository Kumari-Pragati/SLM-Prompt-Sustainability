import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -17)

    def test_boundary_condition(self):
        self.assertEqual(parabola_directrix(0, 0, 0), 0)

    def test_negative_coefficients(self):
        self.assertEqual(parabola_directrix(-1, -2, -3), 17)

    def test_large_coefficients(self):
        self.assertEqual(parabola_directrix(1000, 2000, 3000), -12000001)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 'b', 'c')
