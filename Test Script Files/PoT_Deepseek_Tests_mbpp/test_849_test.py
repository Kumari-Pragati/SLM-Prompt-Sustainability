import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 4)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 7)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 8)
        self.assertEqual(Sum(9), 9)
        self.assertEqual(Sum(10), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(100), 106)
        self.assertEqual(Sum(1000), 1741)
        self.assertEqual(Sum(10000), 17701)

    def test_corner_cases(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(-1), 0)
        self.assertEqual(Sum(-10), 0)
        self.assertEqual(Sum(100000), 177231)
