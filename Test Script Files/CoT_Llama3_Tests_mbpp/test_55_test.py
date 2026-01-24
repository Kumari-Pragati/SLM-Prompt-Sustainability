import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tn_gp(10, 5, 0.1), 10 * math.pow(0.1, 4))

    def test_edge_case_n_zero(self):
        self.assertEqual(tn_gp(10, 0, 0.1), 0)

    def test_edge_case_r_zero(self):
        self.assertEqual(tn_gp(10, 5, 0), 0)

    def test_edge_case_a_zero(self):
        self.assertEqual(tn_gp(0, 5, 0.1), 0)

    def test_invalid_input_non_numeric_a(self):
        with self.assertRaises(TypeError):
            tn_gp('a', 5, 0.1)

    def test_invalid_input_non_numeric_r(self):
        with self.assertRaises(TypeError):
            tn_gp(10, 5, 'r')

    def test_invalid_input_non_numeric_n(self):
        with self.assertRaises(TypeError):
            tn_gp(10, 'n', 0.1)
