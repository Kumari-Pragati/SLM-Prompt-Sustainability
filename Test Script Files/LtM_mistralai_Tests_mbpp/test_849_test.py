import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(4), 3)
        self.assertEqual(Sum(6), 6)
        self.assertEqual(Sum(8), 8)
        self.assertEqual(Sum(10), 15)

    def test_edge_cases(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(25), 150)
        self.assertEqual(Sum(100), 642)
        self.assertEqual(Sum(1000), 33164)

    def test_complex(self):
        self.assertEqual(Sum(13), 12)
        self.assertEqual(Sum(20), 91)
        self.assertEqual(Sum(29), 29)
        self.assertEqual(Sum(31), 31)
        self.assertEqual(Sum(41), 82)
        self.assertEqual(Sum(59), 118)
        self.assertEqual(Sum(71), 142)
        self.assertEqual(Sum(101), 252)
        self.assertEqual(Sum(1009), 25246)
