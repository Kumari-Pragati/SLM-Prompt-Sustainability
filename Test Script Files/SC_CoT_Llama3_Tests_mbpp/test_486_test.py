import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.125, places=3)

    def test_edge_cases(self):
        self.assertAlmostEqual(binomial_probability(1, 1, 0.5), 0.5, places=3)
        self.assertAlmostEqual(binomial_probability(10, 0, 0.5), 0.0, places=3)
        self.assertAlmostEqual(binomial_probability(10, 10, 0.5), 0.5, places=3)

    def test_boundary_cases(self):
        self.assertAlmostEqual(binomial_probability(10, 1, 0.5), 0.5, places=3)
        self.assertAlmostEqual(binomial_probability(10, 9, 0.5), 0.5, places=3)

    def test_special_cases(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 0.0), 0.0, places=3)
        self.assertAlmostEqual(binomial_probability(10, 5, 1.0), 1.0, places=3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binomial_probability('a', 3, 0.5)
        with self.assertRaises(TypeError):
            binomial_probability(10, 'b', 0.5)
        with self.assertRaises(TypeError):
            binomial_probability(10, 3, 'c')
