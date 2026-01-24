import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -5)

    def test_edge_case_a_zero(self):
        self.assertEqual(parabola_directrix(0, 2, 3), -3)

    def test_edge_case_b_zero(self):
        self.assertEqual(parabola_directrix(1, 0, 3), -3)

    def test_edge_case_c_zero(self):
        self.assertEqual(parabola_directrix(1, 2, 0), 0)

    def test_invalid_input_type_a(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 2, 3)

    def test_invalid_input_type_b(self):
        with self.assertRaises(TypeError):
            parabola_directrix(1, 'b', 3)

    def test_invalid_input_type_c(self):
        with self.assertRaises(TypeError):
            parabola_directrix(1, 2, 'c')
