import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(jacobsthal_lucas(2), 6)
        self.assertEqual(jacobsthal_lucas(3), 14)

    def test_complex_cases(self):
        self.assertEqual(jacobsthal_lucas(10), 16382)
        self.assertEqual(jacobsthal_lucas(20), 1048574)
