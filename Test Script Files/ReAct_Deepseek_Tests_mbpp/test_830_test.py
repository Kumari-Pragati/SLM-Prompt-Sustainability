import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(round_up(123.456, 2), 123.46)
        self.assertEqual(round_up(123.454, 2), 123.46)
        self.assertEqual(round_up(123.450, 2), 123.45)
        self.assertEqual(round_up(123.456, 1), 123.5)
        self.assertEqual(round_up(123.449, 1), 123.5)
        self.assertEqual(round_up(123.440, 1), 123.4)

    def test_edge_cases(self):
        self.assertEqual(round_up(0.001, 3), 0.001)
        self.assertEqual(round_up(0.000, 3), 0.000)
        self.assertEqual(round_up(123.456, 0), 124.0)
        self.assertEqual(round_up(123.449, 0), 124.0)
        self.assertEqual(round_up(123.440, 0), 124.0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            round_up('123.456', 2)
        with self.assertRaises(ValueError):
            round_up(123.456, -1)
        with self.assertRaises(TypeError):
            round_up(123.456, '2')
