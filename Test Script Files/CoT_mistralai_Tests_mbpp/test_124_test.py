import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_positive_real_numbers(self):
        self.assertAlmostEqual(angle_complex(3, 0), 0)
        self.assertAlmostEqual(angle_complex(4, 0), 0)

    def test_positive_imaginary_numbers(self):
        self.assertAlmostEqual(angle_complex(0, 3), 90)
        self.assertAlmostEqual(angle_complex(0, 4), 90)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(angle_complex(2, 3), 109.49046378906249)
        self.assertAlmostEqual(angle_complex(2, -3), -109.49046378906249)

    def test_zero_input(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(angle_complex(-2, 3), 71.56243787797942)
        self.assertAlmostEqual(angle_complex(-2, -3), -71.56243787797942)

    def test_large_numbers(self):
        self.assertAlmostEqual(angle_complex(1e6, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1e6), 90)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, angle_complex, 'a', 'b')
        self.assertRaises(TypeError, angle_complex, 3, 'b')
