import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(maximum_Sum([1, 2, 3]), 6)
        self.assertEqual(maximum_Sum([-1, -2, -3]), 3)
        self.assertEqual(maximum_Sum([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(maximum_Sum([]), 0)
        self.assertEqual(maximum_Sum([1]), 1)
        self.assertEqual(maximum_Sum([-1]), -1)
        self.assertEqual(maximum_Sum([100000]), 100000)
        self.assertEqual(maximum_Sum([-100000]), -100000)

    def test_complex_cases(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [-1, -2, -3]]), 6)
        self.assertEqual(maximum_Sum([[-1, -2, -3], [1, 2, 3]]), 6)
        self.assertEqual(maximum_Sum([[-1, -2, -3], [1, 2, -4]]), 3)
        self.assertEqual(maximum_Sum([[-1, -2, -3], [1, 2, 3, 4]]), 7)
