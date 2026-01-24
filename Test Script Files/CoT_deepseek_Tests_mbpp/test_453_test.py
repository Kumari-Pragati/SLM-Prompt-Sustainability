import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sumofFactors(12), 12)
        self.assertEqual(sumofFactors(24), 30)
        self.assertEqual(sumofFactors(36), 55)

    def test_edge_cases(self):
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(1), 0)
        self.assertEqual(sumofFactors(2), 0)
        self.assertEqual(sumofFactors(3), 0)
        self.assertEqual(sumofFactors(4), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sumofFactors("abc")
        with self.assertRaises(TypeError):
            sumofFactors(None)
        with self.assertRaises(TypeError):
            sumofFactors([1,2,3])
