import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(round_up(123.456, 2), 123.46)

    def test_zero_digits(self):
        self.assertEqual(round_up(123.456, 0), 124)

    def test_negative_digits(self):
        self.assertEqual(round_up(123.456, -1), 200)

    def test_large_number(self):
        self.assertAlmostEqual(round_up(123456789.123, 2), 123456789.13)

    def test_small_number(self):
        self.assertAlmostEqual(round_up(0.000123, 2), 0.000124)

    def test_negative_number(self):
        self.assertAlmostEqual(round_up(-123.456, 2), -123.45)

    def test_zero(self):
        self.assertEqual(round_up(0, 2), 0)

    def test_large_digits(self):
        self.assertEqual(round_up(123.456, 10), 123.456)

    def test_invalid_digits(self):
        with self.assertRaises(TypeError):
            round_up(123.456, 'two')
