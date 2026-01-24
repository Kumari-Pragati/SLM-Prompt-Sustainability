import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(jacobsthal_lucas(5), 48)

    def test_boundary_conditions(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)

    def test_negative_input(self):
        with self.assertRaises(IndexError):
            jacobsthal_lucas(-1)

    def test_large_input(self):
        self.assertEqual(jacobsthal_lucas(20), 1048575)
