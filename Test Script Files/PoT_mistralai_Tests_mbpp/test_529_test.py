import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 4)
        self.assertEqual(jacobsthal_lucas(4), 7)
        self.assertEqual(jacobsthal_lucas(5), 11)
        self.assertEqual(jacobsthal_lucas(6), 18)
        self.assertEqual(jacobsthal_lucas(7), 29)
        self.assertEqual(jacobsthal_lucas(8), 47)
        self.assertEqual(jacobsthal_lucas(9), 76)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(jacobsthal_lucas(-1), None)
        self.assertEqual(jacobsthal_lucas(10), 159)
        self.assertEqual(jacobsthal_lucas(20), 3171)
        self.assertEqual(jacobsthal_lucas(30), 54075)
        self.assertEqual(jacobsthal_lucas(40), 927465)
        self.assertEqual(jacobsthal_lucas(50), 16796807)
