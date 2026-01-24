import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(tn_gp(2, 3, 2), 4.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(tn_gp(1, 1, 1), 1.0)
        self.assertAlmostEqual(tn_gp(1, 1, 0), 1.0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(tn_gp(1, 0, 2), 1.0)
        self.assertAlmostEqual(tn_gp(1, 1, 0), 1.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tn_gp('a', 2, 2)
        with self.assertRaises(TypeError):
            tn_gp(2, 'b', 2)
        with self.assertRaises(TypeError):
            tn_gp(2, 2, 'c')
