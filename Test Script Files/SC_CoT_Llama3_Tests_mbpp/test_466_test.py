import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_low(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 1), 0)

    def test_edge_high(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_equal(self):
        self.assertEqual(find_peak([1, 2, 3, 3, 5], 5), 2)

    def test_edge_low_equal(self):
        self.assertEqual(find_peak([1, 1, 2, 3, 5], 5), 0)

    def test_edge_high_equal(self):
        self.assertEqual(find_peak([1, 2, 3, 3, 5], 5), 2)

    def test_edge_low_high_equal(self):
        self.assertEqual(find_peak([1, 1, 2, 2, 2], 5), 0)

    def test_edge_high_high_equal(self):
        self.assertEqual(find_peak([1, 2, 2, 2, 5], 5), 2)

    def test_edge_low_high(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_high_high(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_low_low(self):
        self.assertEqual(find_peak([1, 1, 1, 1, 1], 5), 0)

    def test_edge_high_high(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_low_equal_low(self):
        self.assertEqual(find_peak([1, 1, 1, 1, 1], 5), 0)

    def test_edge_high_equal_high(self):
        self.assertEqual(find_peak([1, 2, 3, 3, 5], 5), 2)

    def test_edge_low_equal_high(self):
        self.assertEqual(find_peak([1, 1, 2, 3, 5], 5), 0)

    def test_edge_high_equal_low(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_low_low_equal(self):
        self.assertEqual(find_peak([1, 1, 1, 1, 1], 5), 0)

    def test_edge_high_high_equal(self):
        self.assertEqual(find_peak([1, 2, 3, 3, 5], 5), 2)

    def test_edge_low_low_high(self):
        self.assertEqual(find_peak([1, 1, 2, 3, 5], 5), 0)

    def test_edge_high_high_low(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_low_low_low(self):
        self.assertEqual(find_peak([1, 1, 1, 1, 1], 5), 0)

    def test_edge_high_high_high(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_low_low_low_equal(self):
        self.assertEqual(find_peak([1, 1, 1, 1, 1], 5), 0)

    def test_edge_high_high_high_equal(self):
        self.assertEqual(find_peak([1, 2, 3, 3, 5], 5), 2)

    def test_edge_low_low_low_high(self):
        self.assertEqual(find_peak([1, 1, 2, 3, 5], 5), 0)

    def test_edge_high_high_high_low(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)
