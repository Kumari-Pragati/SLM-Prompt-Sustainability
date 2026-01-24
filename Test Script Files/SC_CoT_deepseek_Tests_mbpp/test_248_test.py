import unittest
from mbpp_248_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(harmonic_sum(5), 2.283334105, places=6)

    def test_boundary_case(self):
        self.assertEqual(harmonic_sum(1), 1)

    def test_edge_case(self):
        self.assertEqual(harmonic_sum(0), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            harmonic_sum('five')
