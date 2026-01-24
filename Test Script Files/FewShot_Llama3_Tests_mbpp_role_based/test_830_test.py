import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_round_up_positive_numbers(self):
        self.assertEqual(round_up(1.5, 0), 2)
        self.assertEqual(round_up(1.5, 1), 2.0)
        self.assertEqual(round_up(1.5, 2), 1.5)

    def test_round_up_negative_numbers(self):
        self.assertEqual(round_up(-1.5, 0), -2)
        self.assertEqual(round_up(-1.5, 1), -2.0)
        self.assertEqual(round_up(-1.5, 2), -1.5)

    def test_round_up_zero(self):
        self.assertEqual(round_up(0, 0), 0)
        self.assertEqual(round_up(0, 1), 0.0)
        self.assertEqual(round_up(0, 2), 0.0)

    def test_round_up_large_numbers(self):
        self.assertEqual(round_up(1000.5, 0), 1001)
        self.assertEqual(round_up(1000.5, 1), 1001.0)
        self.assertEqual(round_up(1000.5, 2), 1000.5)

    def test_round_up_invalid_digits(self):
        with self.assertRaises(TypeError):
            round_up(1.5, 'a')
