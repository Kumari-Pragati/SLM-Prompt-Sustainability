import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sumofFactors(12), 28)
        self.assertEqual(sumofFactors(24), 60)
        self.assertEqual(sumofFactors(36), 117)

    def test_edge_cases(self):
        self.assertEqual(sumofFactors(1), 0)
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(2), 0)
        self.assertEqual(sumofFactors(3), 0)
        self.assertEqual(sumofFactors(4), 3)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            sumofFactors("abc")
        with self.assertRaises(ValueError):
            sumofFactors(-1)
