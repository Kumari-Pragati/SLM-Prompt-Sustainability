import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(smallest_missing([-1, 0, 1, 2, 3], -1, 3), 4)
        self.assertEqual(smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9), 10)

    def test_edge_conditions(self):
        self.assertEqual(smallest_missing([], -1, 0), -1)
        self.assertEqual(smallest_missing([0], 0, 0))
        self.assertEqual(smallest_missing([1, 2, 3, 4, 5], 1, 5), 0)

    def test_complex_cases(self):
        self.assertEqual(smallest_missing([-1, 0, 1, 2, 3, 5, 6, 7, 8, 9], -1, 9), 4)
        self.assertEqual(smallest_missing([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], -1, 20), 21)
