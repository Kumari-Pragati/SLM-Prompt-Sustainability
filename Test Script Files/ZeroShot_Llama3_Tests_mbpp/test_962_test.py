import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_sum_even(self):
        self.assertEqual(sum_Even(1, 5), 9)
        self.assertEqual(sum_Even(2, 5), 14)
        self.assertEqual(sum_Even(3, 5), 18)
        self.assertEqual(sum_Even(4, 5), 21)
        self.assertEqual(sum_Even(5, 5), 15)
        self.assertEqual(sum_Even(1, 10), 25)
        self.assertEqual(sum_Even(2, 10), 36)
        self.assertEqual(sum_Even(3, 10), 45)
        self.assertEqual(sum_Even(4, 10), 55)
        self.assertEqual(sum_Even(5, 10), 45)
        self.assertEqual(sum_Even(6, 10), 45)
        self.assertEqual(sum_Even(7, 10), 36)
        self.assertEqual(sum_Even(8, 10), 25)
        self.assertEqual(sum_Even(9, 10), 25)
        self.assertEqual(sum_Even(10, 10), 25)

    def test_sum_even_edge_cases(self):
        self.assertEqual(sum_Even(1, 1), 0)
        self.assertEqual(sum_Even(2, 2), 1)
        self.assertEqual(sum_Even(3, 3), 2)
        self.assertEqual(sum_Even(4, 4), 3)
        self.assertEqual(sum_Even(5, 5), 5)
