import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(round_up(1.234, 2), 1.23)
        self.assertEqual(round_up(123.456, 3), 123.46)
        self.assertEqual(round_up(12345.678, 4), 12345.68)

    def test_edge_cases(self):
        self.assertEqual(round_up(1.0, 0), 1)
        self.assertEqual(round_up(123.0, 0), 123)
        self.assertEqual(round_up(12345.0, 0), 12345)

    def test_boundary_cases(self):
        self.assertEqual(round_up(1.234, 1), 1.2)
        self.assertEqual(round_up(123.456, 2), 123.46)
        self.assertEqual(round_up(12345.678, 3), 12345.68)

    def test_special_cases(self):
        self.assertEqual(round_up(-1.234, 2), -1.23)
        self.assertEqual(round_up(-123.456, 3), -123.46)
        self.assertEqual(round_up(-12345.678, 4), -12345.68)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_up('a', 2)
        with self.assertRaises(TypeError):
            round_up(123, 'b')
