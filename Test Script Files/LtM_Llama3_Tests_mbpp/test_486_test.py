import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_simple(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.125)

    def test_edge_case1(self):
        self.assertAlmostEqual(binomial_probability(10, 0, 0.5), 0.0)

    def test_edge_case2(self):
        self.assertAlmostEqual(binomial_probability(10, 10, 0.5), 0.0)

    def test_edge_case3(self):
        self.assertAlmostEqual(binomial_probability(10, 10, 1.0), 0.0)

    def test_edge_case4(self):
        self.assertAlmostEqual(binomial_probability(10, 0, 1.0), 1.0)

    def test_edge_case5(self):
        self.assertAlmostEqual(binomial_probability(10, 10, 0.0), 0.0)

    def test_edge_case6(self):
        self.assertAlmostEqual(binomial_probability(10, 0, 0.0), 0.0)

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            binomial_probability('a', 3, 0.5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            binomial_probability(10, 'b', 0.5)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            binomial_probability(10, 3, 'c')
