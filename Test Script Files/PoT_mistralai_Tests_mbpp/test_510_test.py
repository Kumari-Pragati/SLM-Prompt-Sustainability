import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)
        self.assertEqual(no_of_subsequences([1, 1, 1, 1, 1], 1), 5)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 6), 7)

    def test_edge_case(self):
        self.assertEqual(no_of_subsequences([], 1), 0)
        self.assertEqual(no_of_subsequences([1], 1), 1)
        self.assertEqual(no_of_subsequences([1], 2), 1)
        self.assertEqual(no_of_subsequences([1, 1], 1), 1)
        self.assertEqual(no_of_subsequences([1, 1], 2), 2)

    def test_boundary_case(self):
        self.assertEqual(no_of_subsequences([0], 1), 0)
        self.assertEqual(no_of_subsequences([1, 0], 1), 1)
        self.assertEqual(no_of_subsequences([1, 0], 2), 2)
        self.assertEqual(no_of_subsequences([0, 0], 1), 0)
        self.assertEqual(no_of_subsequences([0, 0], 2), 1)
