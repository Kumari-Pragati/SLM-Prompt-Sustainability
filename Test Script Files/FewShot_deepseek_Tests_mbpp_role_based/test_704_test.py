import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(harmonic_sum(5), 2.28333410306, places=7)

    def test_boundary_condition(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_edge_condition(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            harmonic_sum('5')
