import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_jacobsthal_lucas_typical(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 5)
        self.assertEqual(jacobsthal_lucas(4), 8)
        self.assertEqual(jacobsthal_lucas(5), 13)

    def test_jacobsthal_lucas_edge(self):
        self.assertEqual(jacobsthal_lucas(-1), None)
        self.assertEqual(jacobsthal_lucas(-2), None)
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(2), 3)
        self.assertEqual(jacobsthal_lucas(3), 5)
        self.assertEqual(jacobsthal_lucas(4), 8)
        self.assertEqual(jacobsthal_lucas(5), 13)

    def test_jacobsthal_lucas_invalid(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas('a')
        with self.assertRaises(TypeError):
            jacobsthal_lucas(None)
        with self.assertRaises(TypeError):
            jacobsthal_lucas(1.5)
