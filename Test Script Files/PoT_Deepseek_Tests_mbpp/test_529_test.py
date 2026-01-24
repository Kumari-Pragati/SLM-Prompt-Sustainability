import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(5), 136)
        self.assertEqual(jacobsthal_lucas(10), 20476)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_lucas(-1), 2)
        self.assertEqual(jacobsthal_lucas(0), 2)

    def test_corner_cases(self):
        self.assertEqual(jacobsthal_lucas(20), 1048575)
