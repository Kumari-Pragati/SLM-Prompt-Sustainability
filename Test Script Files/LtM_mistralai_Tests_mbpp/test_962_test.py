import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_Even(2, 4), 6)
        self.assertEqual(sum_Even(4, 6), 12)
        self.assertEqual(sum_Even(6, 8), 20)

    def test_edge_and_boundary(self):
        self.assertEqual(sum_Even(1, 2), 0)
        self.assertEqual(sum_Even(2, 1), 0)
        self.assertEqual(sum_Even(0, 2), 0)
        self.assertEqual(sum_Even(2, 0), 0)
        self.assertEqual(sum_Even(1, 1), 0)
        self.assertEqual(sum_Even(2, 3), 2)
        self.assertEqual(sum_Even(3, 2), 2)

    def test_complex(self):
        self.assertEqual(sum_Even(10, 20), 330)
        self.assertEqual(sum_Even(20, 30), 660)
        self.assertEqual(sum_Even(30, 40), 1090)
        self.assertEqual(sum_Even(40, 50), 1620)
        self.assertEqual(sum_Even(50, 60), 2250)
