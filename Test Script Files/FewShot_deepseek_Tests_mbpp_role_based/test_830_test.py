import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(round_up(123.456, 2), 123.46)

    def test_zero_digits(self):
        self.assertEqual(round_up(123.456, 0), 124.0)

    def test_negative_digits(self):
        self.assertEqual(round_up(123.456, -1), 130.0)

    def test_boundary_conditions(self):
        self.assertEqual(round_up(0.0, 2), 0.0)
        self.assertEqual(round_up(123.456, 3), 123.456)

    def test_large_numbers(self):
        self.assertEqual(round_up(123456789.123, 2), 123456789.13)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_up('123.456', 2)
        with self.assertRaises(TypeError):
            round_up(123.456, '2')
        with self.assertRaises(ValueError):
            round_up(123.456, -4)
