import unittest
from mbpp_486_code import binomial_probability, nCr

class TestBinomialProbability(unittest.TestCase):

    def test_binomial_probability_basic(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.14050946356487897)
        self.assertAlmostEqual(binomial_probability(5, 2, 0.7), 0.3846153846153846)
        self.assertAlmostEqual(binomial_probability(20, 10, 0.3), 0.10737418254589549)

    def test_binomial_probability_edge_cases(self):
        self.assertAlmostEqual(binomial_probability(0, 0, 0), 1)
        self.assertAlmostEqual(binomial_probability(0, 1, 0), 0)
        self.assertAlmostEqual(binomial_probability(1, 0, 0), 0)
        self.assertAlmostEqual(binomial_probability(1, 1, 1), 0)

    def test_nCr(self):
        self.assertEqual(nCr(5, 2), 10)
        self.assertEqual(nCr(10, 4), 210)
        self.assertEqual(nCr(20, 10), 184756)
