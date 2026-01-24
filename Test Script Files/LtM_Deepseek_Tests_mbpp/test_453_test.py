import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(sumofFactors(12), 12)
        self.assertEqual(sumofFactors(24), 36)
        self.assertEqual(sumofFactors(36), 55)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(1), 0)
        self.assertEqual(sumofFactors(2), 2)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(sumofFactors(100), 117)
        self.assertEqual(sumofFactors(1000), 1320)
        self.assertEqual(sumofFactors(10000), 13860)
