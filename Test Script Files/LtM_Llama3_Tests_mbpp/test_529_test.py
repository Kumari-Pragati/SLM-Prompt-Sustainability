import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 5)
        self.assertEqual(jacobsthal_lucas(4), 8)

    def test_edge(self):
        self.assertEqual(jacobsthal_lucas(-1), None)
        self.assertEqual(jacobsthal_lucas(-2), None)
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 5)
        self.assertEqual(jacobsthal_lucas(4), 8)

    def test_larger(self):
        self.assertEqual(jacobsthal_lucas(5), 13)
        self.assertEqual(jacobsthal_lucas(6), 21)
        self.assertEqual(jacobsthal_lucas(7), 34)
        self.assertEqual(jacobsthal_lucas(8), 55)
        self.assertEqual(jacobsthal_lucas(9), 89)
