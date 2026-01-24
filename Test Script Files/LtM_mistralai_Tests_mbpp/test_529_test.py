import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 4)
        self.assertEqual(jacobsthal_lucas(4), 9)

    def test_edge_and_boundary(self):
        self.assertEqual(jacobsthal_lucas(5), 20)
        self.assertEqual(jacobsthal_lucas(6), 21)
        self.assertEqual(jacobsthal_lucas(7), 42)
        self.assertEqual(jacobsthal_lucas(8), 45)
        self.assertEqual(jacobsthal_lucas(9), 94)
        self.assertEqual(jacobsthal_lucas(10), 99)

    def test_complex(self):
        self.assertEqual(jacobsthal_lucas(11), 193)
        self.assertEqual(jacobsthal_lucas(12), 199)
        self.assertEqual(jacobsthal_lucas(13), 387)
        self.assertEqual(jacobsthal_lucas(14), 409)
        self.assertEqual(jacobsthal_lucas(15), 816)
        self.assertEqual(jacobsthal_lucas(16), 833)
        self.assertEqual(jacobsthal_lucas(17), 1633)
        self.assertEqual(jacobsthal_lucas(18), 1661)
        self.assertEqual(jacobsthal_lucas(19), 3258)
        self.assertEqual(jacobsthal_lucas(20), 3297)
