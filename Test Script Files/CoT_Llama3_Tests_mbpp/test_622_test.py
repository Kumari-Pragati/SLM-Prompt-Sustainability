import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_edge_case(self):
        self.assertAlmostEqual(get_median([1, 2, 3], [], 3), 2)

    def test_edge_case2(self):
        self.assertAlmostEqual(get_median([], [1, 2, 3], 3), 2)

    def test_edge_case3(self):
        self.assertAlmostEqual(get_median([1, 2, 3], [4, 5, 6], 3), 3)

    def test_edge_case4(self):
        self.assertAlmostEqual(get_median([1, 2, 3, 4, 5, 6], [], 6), 3.5)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            get_median([1, 2, 3], [4, 5], 2)
