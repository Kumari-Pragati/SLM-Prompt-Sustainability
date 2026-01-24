import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -11)

    def test_edge_case_a_zero(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_directrix(0, 2, 3)

    def test_edge_case_b_zero(self):
        self.assertEqual(parabola_directrix(1, 0, 3), -3)

    def test_edge_case_c_zero(self):
        self.assertEqual(parabola_directrix(1, 2, 0), 0)

    def test_edge_case_c_negative(self):
        self.assertEqual(parabola_directrix(1, 2, -3), -12)

    def test_edge_case_c_positive(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -11)

    def test_edge_case_b_positive(self):
        self.assertEqual(parabola_directrix(1, 3, 3), -15)

    def test_edge_case_b_negative(self):
        self.assertEqual(parabola_directrix(1, -3, 3), -9)
