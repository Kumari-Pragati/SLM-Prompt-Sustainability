import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(get_median([1, 3], [2], 2), 2.0)
        self.assertAlmostEqual(get_median([1, 2, 3, 4], [2, 3, 4, 5], 4), 2.5)

    def test_edge_conditions(self):
        self.assertAlmostEqual(get_median([1], [], 1), 1.0)
        self.assertAlmostEqual(get_median([], [1], 1), 1.0)
        self.assertAlmostEqual(get_median([1, 2], [1, 2], 2), 1.5)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(get_median([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 3.0)
        self.assertAlmostEqual(get_median([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], 6), 3.0)

    def test_complex_cases(self):
        self.assertAlmostEqual(get_median([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), 5.0)
