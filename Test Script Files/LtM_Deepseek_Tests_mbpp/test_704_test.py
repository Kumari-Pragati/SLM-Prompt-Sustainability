import unittest
from mbpp_704_code import harmonic_sum

class TestHarmonicSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(harmonic_sum(1), 1)
        self.assertAlmostEqual(harmonic_sum(2), 1.5)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(harmonic_sum(0), 1)
        self.assertAlmostEqual(harmonic_sum(1), 1)

    def test_edge_cases(self):
        self.assertAlmostEqual(harmonic_sum(10), 2.928968254, places=5)
        self.assertAlmostEqual(harmonic_sum(100), 5.187377517, places=5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            harmonic_sum('a')
        with self.assertRaises(TypeError):
            harmonic_sum(None)
        with self.assertRaises(TypeError):
            harmonic_sum([])
