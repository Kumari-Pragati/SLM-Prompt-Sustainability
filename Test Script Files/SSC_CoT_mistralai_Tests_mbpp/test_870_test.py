import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_positivenum([0, 1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_positivenum([-1, 0, 1, 2, 3, 4, 5]), 15)

    def test_edge_cases(self):
        self.assertEqual(sum_positivenum([0]), 0)
        self.assertEqual(sum_positivenum([-1]), 0)
        self.assertEqual(sum_positivenum([1]), 1)
        self.assertEqual(sum_positivenum([-1, -2]), 0)
        self.assertEqual(sum_positivenum([1, 0]), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_positivenum([-1, 0, 1]), 1)
        self.assertEqual(sum_positivenum([-1, 0, 1, 0]), 1)
        self.assertEqual(sum_positivenum([1, 0, 1, 0]), 2)
        self.assertEqual(sum_positivenum([1, 0, 1, 0, 0]), 2)
