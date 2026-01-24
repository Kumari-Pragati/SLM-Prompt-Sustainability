import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 4)
        self.assertEqual(jacobsthal_lucas(4), 9)
        self.assertEqual(jacobsthal_lucas(5), 20)
        self.assertEqual(jacobsthal_lucas(6), 49)
        self.assertEqual(jacobsthal_lucas(7), 121)
        self.assertEqual(jacobsthal_lucas(8), 302)
        self.assertEqual(jacobsthal_lucas(9), 775)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(jacobsthal_lucas(-1), None)
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2**31 - 1), 2147483647)
        self.assertEqual(jacobsthal_lucas(2**31), None)
