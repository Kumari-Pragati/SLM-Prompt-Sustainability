import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_round_up_positive_numbers(self):
        self.assertEqual(round_up(12.345, 2), 12.34)
        self.assertEqual(round_up(123.456, 3), 123.457)
        self.assertEqual(round_up(1234.567, 0), 1235)
        self.assertEqual(round_up(12345.678, -1), 12346)

    def test_round_up_zero_and_negative_numbers(self):
        self.assertEqual(round_up(0.000, 3), 0.000)
        self.assertEqual(round_up(-12.345, 2), -12.34)
        self.assertEqual(round_up(-123.456, 3), -123.457)
        self.assertEqual(round_up(-1234.567, 0), -1235)
        self.assertEqual(round_up(-12345.678, -1), -12346)

    def test_round_up_invalid_inputs(self):
        self.assertRaises(TypeError, round_up, 'not a number', 2)
        self.assertRaises(ValueError, round_up, -1, -1)
        self.assertRaises(ValueError, round_up, 0, 0)
