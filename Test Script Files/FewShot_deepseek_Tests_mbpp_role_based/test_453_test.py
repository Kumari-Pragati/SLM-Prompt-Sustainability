import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sumofFactors(12), 16)

    def test_edge_case(self):
        self.assertEqual(sumofFactors(2), 2)

    def test_boundary_case(self):
        self.assertEqual(sumofFactors(1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sumofFactors("abc")

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sumofFactors(-10)
