import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_convert_function(self):
        self.assertAlmostEqual(convert(1), (1, 0))
        self.assertAlmostEqual(convert(-1), (1, 3.14159265359))
        self.assertAlmostEqual(convert(0), (0, 0))
        self.assertAlmostEqual(convert(1+1j), (1.4142135623730951, 0.7853981633974483))
        self.assertAlmostEqual(convert(-1-1j), (1.4142135623730951, 4.71238898038469))
        self.assertAlmostEqual(convert(0+0j), (0, 0))

    def test_convert_function_with_negative_numbers(self):
        self.assertAlmostEqual(convert(-1), (1, 3.14159265359))
        self.assertAlmostEqual(convert(-1-1j), (1.4142135623730951, 4.71238898038469))

    def test_convert_function_with_zero(self):
        self.assertAlmostEqual(convert(0), (0, 0))

    def test_convert_function_with_positive_numbers(self):
        self.assertAlmostEqual(convert(1), (1, 0))
        self.assertAlmostEqual(convert(1+1j), (1.4142135623730951, 0.7853981633974483))
