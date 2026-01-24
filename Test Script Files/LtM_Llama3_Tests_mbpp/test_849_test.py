import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 0)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 3)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 5)

    def test_edge(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 0)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 3)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 5)

    def test_complex(self):
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 7)
        self.assertEqual(Sum(9), 7)
        self.assertEqual(Sum(10), 7)
        self.assertEqual(Sum(11), 11)
        self.assertEqual(Sum(12), 11)
