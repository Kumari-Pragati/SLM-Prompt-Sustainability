import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(round_up(1.2345, 2), 1.24)
        self.assertAlmostEqual(round_up(123.456, 1), 124.0)
        self.assertAlmostEqual(round_up(1234.56, 0), 1235.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(round_up(0.0, 1), 0.0)
        self.assertAlmostEqual(round_up(1.0, 0), 2.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(round_up(0.0, 0), 0.0)
        self.assertAlmostEqual(round_up(1.0, 2), 1.0)
        self.assertAlmostEqual(round_up(0.123456, 5), 0.12346)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_up("1.23", 1)
        with self.assertRaises(ValueError):
            round_up(1.23, -1)
