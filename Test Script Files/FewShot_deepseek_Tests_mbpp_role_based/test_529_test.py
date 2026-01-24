import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(jacobsthal_lucas(5), 47)

    def test_boundary_conditions(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(jacobsthal_lucas(2), 5)
        self.assertEqual(jacobsthal_lucas(3), 11)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas('5')
        with self.assertRaises(ValueError):
            jacobsthal_lucas(-5)
