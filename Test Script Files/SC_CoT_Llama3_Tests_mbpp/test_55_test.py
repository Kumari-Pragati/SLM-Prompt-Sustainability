import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(tn_gp(10, 5, 0.1), 10 * (0.1 ** (5 - 1)))
    def test_edge_cases(self):
        self.assertEqual(tn_gp(10, 0, 0.1), 0)
        self.assertEqual(tn_gp(10, 1, 0.1), 10 * (0.1 ** 0))
    def test_boundary_cases(self):
        self.assertEqual(tn_gp(10, 2, 0.1), 10 * (0.1 ** 1))
        self.assertEqual(tn_gp(10, 3, 0.1), 10 * (0.1 ** 2))
    def test_special_cases(self):
        self.assertEqual(tn_gp(10, -1, 0.1), 0)
        self.assertEqual(tn_gp(10, 5, 0), 0)
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tn_gp('a', 5, 0.1)
        with self.assertRaises(TypeError):
            tn_gp(10, 'b', 0.1)
        with self.assertRaises(TypeError):
            tn_gp(10, 5, 'c')
