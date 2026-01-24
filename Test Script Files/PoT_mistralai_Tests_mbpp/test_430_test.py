import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parabola_directrix(1, 2, 5), -11)
        self.assertEqual(parabola_directrix(2, 3, 10), 17)
        self.assertEqual(parabola_directrix(3, 4, 15), 3)

    def test_edge_case_zero_a(self):
        self.assertRaises(ZeroDivisionError, parabola_directrix, 0, 1, 2)

    def test_edge_case_negative_a(self):
        self.assertRaises(ValueError, parabola_directrix, -1, 1, 2)

    def test_edge_case_zero_b(self):
        self.assertRaises(ValueError, parabola_directrix, 1, 0, 2)

    def test_edge_case_zero_c(self):
        self.assertRaises(ValueError, parabola_directrix, 1, 2, 0)
