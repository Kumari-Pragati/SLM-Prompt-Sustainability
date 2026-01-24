import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_low(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case_high(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_equal(self):
        self.assertEqual(find_peak([1, 2, 2, 4, 5], 5), 2)

    def test_edge_case_first(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case_last(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_peak([], 5)
