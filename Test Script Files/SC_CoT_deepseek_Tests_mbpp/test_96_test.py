import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(4), 3)
        self.assertEqual(divisor(10), 4)

    def test_edge_cases(self):
        self.assertEqual(divisor(0), 1)
        self.assertEqual(divisor(1), 1)

    def test_corner_cases(self):
        self.assertEqual(divisor(9999), 9999)
        self.assertEqual(divisor(10000), 10000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            divisor('a')
        with self.assertRaises(TypeError):
            divisor(None)
        with self.assertRaises(TypeError):
            divisor([])
        with self.assertRaises(TypeError):
            divisor({})
