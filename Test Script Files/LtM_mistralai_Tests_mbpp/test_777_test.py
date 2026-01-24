import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(find_Sum([5, 5, 6], 3), 11)
        self.assertEqual(find_Sum([0, 0, 1], 3), 1)

    def test_edge_cases(self):
        self.assertEqual(find_Sum([], 0), 0)
        self.assertEqual(find_Sum([1], 1), 1)
        self.assertEqual(find_Sum([1, 1], 2), 1)
        self.assertEqual(find_Sum([1, 2, 1], 3), 3)
        self.assertEqual(find_Sum([1, 2, 3, 4, 1], 5), 10)

    def test_complex_cases(self):
        self.assertEqual(find_Sum([1, 2, 1, 2, 3, 2, 4, 2, 3, 5], 10), 21)
        self.assertEqual(find_Sum([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5], 10), 0)
        self.assertEqual(find_Sum([1000000001, 1000000002, 1000000003], 3), 600000005)
