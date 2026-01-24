import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(round_up(1.2345, 2), 1.24)
        self.assertEqual(round_up(123.456, 1), 123.5)
        self.assertEqual(round_up(1234.567, 0), 1235.0)

    def test_simple_negative_numbers(self):
        self.assertEqual(round_up(-1.2345, 2), -1.23)
        self.assertEqual(round_up(-123.456, 1), -123.4)
        self.assertEqual(round_up(-1234.567, 0), -1234.0)

    def test_edge_cases(self):
        self.assertEqual(round_up(0, 2), 0.0)
        self.assertEqual(round_up(0, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(round_up(1.2345, 5), 1.23450)
        self.assertEqual(round_up(1.2345, -1), 0)

    def test_complex_cases(self):
        self.assertEqual(round_up(1234.5678, 3), 1234.568)
        self.assertEqual(round_up(0.00001, 2), 0.00)
