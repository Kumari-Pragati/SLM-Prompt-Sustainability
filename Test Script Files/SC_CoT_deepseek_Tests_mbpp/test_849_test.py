import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Sum(6), 10)

    def test_boundary_case(self):
        self.assertEqual(Sum(1), 0)

    def test_edge_case(self):
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(5), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Sum("6")
        with self.assertRaises(ValueError):
            Sum(-6)
