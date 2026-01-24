import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 2)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 3)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 3)
        self.assertEqual(Sum(9), 3)
        self.assertEqual(Sum(10), 5)

    def test_edge_input(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(100000), 142913828922)

    def test_boundary_input(self):
        self.assertEqual(Sum(100001), 142913828922)
        self.assertEqual(Sum(2147483647), 2147483647)

    def test_invalid_input(self):
        self.assertRaises(TypeError, Sum, 'not_a_number')
        self.assertRaises(TypeError, Sum, -1)
        self.assertRaises(TypeError, Sum, float('nan'))
        self.assertRaises(TypeError, Sum, complex(1, 2))
