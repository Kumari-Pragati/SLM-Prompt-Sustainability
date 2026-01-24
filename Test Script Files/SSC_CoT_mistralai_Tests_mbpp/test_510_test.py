import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)
        self.assertEqual(no_of_subsequences([4, 4, 4, 4], 1), 13)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 6), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(no_of_subsequences([], 1), 0)
        self.assertEqual(no_of_subsequences([1], 1), 1)
        self.assertEqual(no_of_subsequences([1, 1], 2), 2)
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)
        self.assertEqual(no_of_subsequences([1, 2, 3], 5), 10)
        self.assertEqual(no_of_subsequences([1, 2, 3], 7), 21)

    def test_negative_numbers(self):
        self.assertEqual(no_of_subsequences([-1, 2, 3], 3), 6)
        self.assertEqual(no_of_subsequences([-1, -2, -3], 1), 3)

    def test_zero_numbers(self):
        self.assertEqual(no_of_subsequences([0, 2, 3], 3), 6)
        self.assertEqual(no_of_subsequences([0, 0, 3], 3), 3)
