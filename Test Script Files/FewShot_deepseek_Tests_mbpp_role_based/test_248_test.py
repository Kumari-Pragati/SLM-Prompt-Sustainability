import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(harmonic_sum(5), 2.28333410307, places=7)

    def test_boundary_condition_1(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_boundary_condition_2(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_edge_condition(self):
        self.assertEqual(harmonic_sum(-1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            harmonic_sum('a')
