import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_round_up_positive_numbers(self):
        self.assertEqual(round_up(12.3456, 2), 12.34)
        self.assertEqual(round_up(12.345678, 3), 12.346)
        self.assertEqual(round_up(12.3456789, 4), 12.3457)

    def test_round_up_zero(self):
        self.assertEqual(round_up(0.0000, 6), 0.0000)

    def test_round_up_negative_numbers(self):
        self.assertEqual(round_up(-12.3456, 2), -12.34)
        self.assertEqual(round_up(-12.345678, 3), -12.346)
        self.assertEqual(round_up(-12.3456789, 4), -12.3457)

    def test_round_up_invalid_digits(self):
        self.assertRaises(ValueError, round_up, 12.3456, -1)
        self.assertRaises(ValueError, round_up, 12.3456, 0)
