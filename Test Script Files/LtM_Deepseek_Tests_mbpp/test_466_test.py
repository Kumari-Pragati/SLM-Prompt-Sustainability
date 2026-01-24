import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_peak([1, 3, 20, 4, 1, 0], 6), 2)

    def test_edge_condition_single_element(self):
        self.assertEqual(find_peak([5], 1), 0)

    def test_edge_condition_decreasing_order(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1], 5), 0)

    def test_edge_condition_increasing_order(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_complex_input(self):
        self.assertEqual(find_peak([1, 6, 5, 9, 10, 8, 7], 7), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_peak("1, 3, 20, 4, 1, 0", 6)
