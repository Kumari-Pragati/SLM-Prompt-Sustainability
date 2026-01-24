import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_divisor_positive(self):
        self.assertEqual(divisor(10), 2)

    def test_divisor_negative(self):
        with self.assertRaises(TypeError):
            divisor(-10)

    def test_divisor_zero(self):
        self.assertEqual(divisor(0), 1)

    def test_divisor_one(self):
        self.assertEqual(divisor(1), 1)

    def test_divisor_large(self):
        self.assertEqual(divisor(100), 2)

    def test_divisor_edge(self):
        self.assertEqual(divisor(1), 1)
