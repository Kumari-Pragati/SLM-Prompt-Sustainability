import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(round_up(1.23456, 2), 1.24)
        self.assertEqual(round_up(1.23456, 1), 1.3)
        self.assertEqual(round_up(1.23456, 0), 2.0)

    def test_negative_numbers(self):
        self.assertEqual(round_up(-1.23456, 2), -1.23)
        self.assertEqual(round_up(-1.23456, 1), -1.2)
        self.assertEqual(round_up(-1.23456, 0), -2.0)

    def test_zero(self):
        self.assertEqual(round_up(0, 2), 0.0)
        self.assertEqual(round_up(0, 1), 0.0)
        self.assertEqual(round_up(0, 0), 0.0)

    def test_large_numbers(self):
        self.assertEqual(round_up(123456.789, 2), 123456.79)
        self.assertEqual(round_up(123456.789, 1), 123456.8)
        self.assertEqual(round_up(123456.789, 0), 123500.0)
