import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(convert(1+1j), (1.4142135623730951, 0.7853981633974483))

    def test_zero_case(self):
        self.assertEqual(convert(0), (0, 0))

    def test_negative_case(self):
        self.assertEqual(convert(-1-1j), (1.4142135623730951, 2.356194490192345))

    def test_real_number_case(self):
        self.assertEqual(convert(2), (2, 0))

    def test_imaginary_number_case(self):
        self.assertEqual(convert(1j), (1, 1.5707963267948966))

    def test_invalid_input_case(self):
        with self.assertRaises(TypeError):
            convert("invalid")
