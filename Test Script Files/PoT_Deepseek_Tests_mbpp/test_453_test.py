import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sumofFactors(12), 28)
        self.assertEqual(sumofFactors(24), 60)
        self.assertEqual(sumofFactors(36), 117)

    def test_edge_cases(self):
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(1), 0)
        self.assertEqual(sumofFactors(2), 0)

    def test_boundary_cases(self):
        self.assertEqual(sumofFactors(453), 1365)
        self.assertEqual(sumofFactors(906), 2718)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sumofFactors("string")
        with self.assertRaises(ValueError):
            sumofFactors(-1)
