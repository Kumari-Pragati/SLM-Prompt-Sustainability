import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(round_up(123.456, 2), 123.46)
        self.assertEqual(round_up(123.456, 1), 123.5)
        self.assertEqual(round_up(123.456, 0), 124.0)

    def test_edge_cases(self):
        self.assertEqual(round_up(0.0, 2), 0.0)
        self.assertEqual(round_up(0.0, 0), 0.0)

    def test_boundary_conditions(self):
        self.assertEqual(round_up(123.456, -1), 120.0)
        self.assertEqual(round_up(123.456, -2), 100.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_up("123.456", 2)
        with self.assertRaises(ValueError):
            round_up(123.456, -3)
