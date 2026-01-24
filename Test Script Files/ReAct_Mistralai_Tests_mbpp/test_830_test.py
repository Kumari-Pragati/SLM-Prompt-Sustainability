import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_round_up_positive_numbers(self):
        self.assertEqual(round_up(10.12345, 2), 10.12)
        self.assertEqual(round_up(123.45678, 3), 123.457)
        self.assertEqual(round_up(1234.56789, 0), 1230)
        self.assertEqual(round_up(12345.67890, -1), 12300)

    def test_round_up_zero(self):
        self.assertEqual(round_up(0.00000, 6), 0.0)

    def test_round_up_negative_numbers(self):
        self.assertEqual(round_up(-10.12345, 2), -10.12)
        self.assertEqual(round_up(-123.45678, 3), -123.457)
        self.assertEqual(round_up(-1234.56789, 0), -1230)
        self.assertEqual(round_up(-12345.67890, -1), -12300)

    def test_round_up_non_numeric_input(self):
        with self.assertRaises(TypeError):
            round_up('not a number', 2)
        with self.assertRaises(TypeError):
            round_up([1, 2, 3], 2)
        with self.assertRaises(TypeError):
            round_up({'a': 1, 'b': 2}, 2)
