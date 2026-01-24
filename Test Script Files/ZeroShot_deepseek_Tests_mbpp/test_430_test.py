import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_positive_a(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -15)

    def test_negative_a(self):
        self.assertEqual(parabola_directrix(-1, 2, 3), 15)

    def test_zero_a(self):
        self.assertEqual(parabola_directrix(0, 2, 3), 3)

    def test_zero_b(self):
        self.assertEqual(parabola_directrix(1, 0, 3), -11)

    def test_zero_c(self):
        self.assertEqual(parabola_directrix(1, 2, 0), -3)

    def test_negative_b(self):
        self.assertEqual(parabola_directrix(1, -2, 3), 15)

    def test_negative_c(self):
        self.assertEqual(parabola_directrix(1, 2, -3), -11)

    def test_negative_a_b_c(self):
        self.assertEqual(parabola_directrix(-1, -2, -3), 15)
