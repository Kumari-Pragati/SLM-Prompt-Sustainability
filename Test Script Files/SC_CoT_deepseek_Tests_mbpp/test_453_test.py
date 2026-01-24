import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sumofFactors(12), 12)

    def test_edge_case(self):
        self.assertEqual(sumofFactors(2), 2)

    def test_boundary_case(self):
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(1), 0)

    def test_special_case(self):
        self.assertEqual(sumofFactors(36), 55)
        self.assertEqual(sumofFactors(100), 110)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sumofFactors("abc")
        with self.assertRaises(ValueError):
            sumofFactors(-10)
