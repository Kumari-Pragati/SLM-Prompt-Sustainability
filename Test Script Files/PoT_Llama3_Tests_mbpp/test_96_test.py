import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(divisor(10), 2)
        self.assertEqual(divisor(12), 3)
        self.assertEqual(divisor(15), 3)

    def test_edge(self):
        self.assertEqual(divisor(1), 0)
        self.assertEqual(divisor(2), 1)
        self.assertEqual(divisor(3), 2)

    def test_boundary(self):
        self.assertEqual(divisor(4), 2)
        self.assertEqual(divisor(5), 2)
        self.assertEqual(divisor(6), 2)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            divisor("a")
        with self.assertRaises(TypeError):
            divisor(None)
