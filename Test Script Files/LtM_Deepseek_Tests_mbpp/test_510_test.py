import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)
        self.assertEqual(no_of_subsequences([1, 2, 3], 4), 6)
        self.assertEqual(no_of_subsequences([1, 2, 3], 1), 1)

    def test_edge_conditions(self):
        self.assertEqual(no_of_subsequences([], 1), 0)
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)
        self.assertEqual(no_of_subsequences([1, 2, 3], -1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(no_of_subsequences([1]*1000, 1), 1000)
        self.assertEqual(no_of_subsequences([1]*1000, 1000), 1000**2)

    def test_complex_cases(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 6), 7)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 10), 15)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 20), 31)
