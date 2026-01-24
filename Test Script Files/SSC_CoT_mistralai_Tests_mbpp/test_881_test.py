import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5]), 3)
        self.assertEqual(sum_even_odd([-2, -1, 0, 1, 2]), 3)

    def test_edge_cases(self):
        self.assertEqual(sum_even_odd([]), -1)
        self.assertEqual(sum_even_odd([0]), 0)
        self.assertEqual(sum_even_odd([2]), 2)
        self.assertEqual(sum_even_odd([-2]), -2)

    def test_boundary_cases(self):
        self.assertEqual(sum_even_odd([-1, 0, 1]), 0)
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5, 6]), 11)

    def test_invalid_input(self):
        self.assertRaises(StopIteration, sum_even_odd, [1])
        self.assertRaises(StopIteration, sum_even_odd, [2, 2])
