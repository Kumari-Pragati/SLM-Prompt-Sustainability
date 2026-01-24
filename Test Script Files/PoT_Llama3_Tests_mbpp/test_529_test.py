import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 4)
        self.assertEqual(jacobsthal_lucas(4), 7)

    def test_edge_case(self):
        self.assertEqual(jacobsthal_lucas(-1), None)
        self.assertEqual(jacobsthal_lucas(-2), None)
        self.assertEqual(jacobsthal_lucas(5), 11)

    def test_boundary_case(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 4)
        self.assertEqual(jacobsthal_lucas(4), 7)
        self.assertEqual(jacobsthal_lucas(5), 11)

    def test_corner_case(self):
        self.assertEqual(jacobsthal_lucas(6), 18)
