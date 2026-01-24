import unittest
from mbpp_252_code import convert
import cmath

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(convert(1 + 1j), cmath.polar(1 + 1j))

    def test_zero_case(self):
        self.assertEqual(convert(0), cmath.polar(0))

    def test_negative_real_case(self):
        self.assertEqual(convert(-1 + 1j), cmath.polar(-1 + 1j))

    def test_negative_imaginary_case(self):
        self.assertEqual(convert(1 - 1j), cmath.polar(1 - 1j))

    def test_large_numbers_case(self):
        self.assertEqual(convert(1000 + 1000j), cmath.polar(1000 + 1000j))

    def test_complex_numbers_case(self):
        self.assertEqual(convert(1 + 2j), cmath.polar(1 + 2j))

    def test_error_case(self):
        with self.assertRaises(TypeError):
            convert("1 + 1j")
