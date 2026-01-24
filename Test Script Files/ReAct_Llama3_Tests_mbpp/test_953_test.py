import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(subset([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(subset([1], 1), 1)

    def test_repeated_elements(self):
        self.assertEqual(subset([1, 1, 1, 2, 2, 3], 6), 3)

    def test_no_repeated_elements(self):
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)

    def test_large_array(self):
        self.assertEqual(subset([1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7], 20), 7)

    def test_edge_case(self):
        self.assertEqual(subset([1], 1), 1)

    def test_edge_case2(self):
        self.assertEqual(subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 20), 20)
