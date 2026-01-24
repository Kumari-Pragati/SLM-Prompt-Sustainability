import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), (1 + 3, 2 + 4))
        self.assertEqual(sum_of_alternates((0, 1, 0, 1, 0)), (1, 0))
        self.assertEqual(sum_of_alternates((-1, 0, 1, 2, -3)), (-1 + 2, 0 + 1 + 2))

    def test_edge_and_boundary_cases(self):
        self.assertEqual(sum_of_alternates(()), (0, 0))
        self.assertEqual(sum_of_alternates((1,)), (1, 0))
        self.assertEqual(sum_of_alternates((1, 1)), (1, 1))
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5, 6)), (1 + 3 + 5, 2 + 4))
