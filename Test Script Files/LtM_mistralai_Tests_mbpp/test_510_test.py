import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)
        self.assertEqual(no_of_subsequences([1, 1, 1, 1], 1), 4)
        self.assertEqual(no_of_subsequences([4, 4, 4, 4, 4], 20), 256)

    def test_edge_case_empty_list(self):
        self.assertEqual(no_of_subsequences([], 1), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(no_of_subsequences([1], 1), 1)
        self.assertEqual(no_of_subsequences([-1], 1), 1)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 4), 0)

    def test_edge_case_k_less_than_1(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)

    def test_negative_elements(self):
        self.assertEqual(no_of_subsequences([-1, -2, -3], 1), 3)
        self.assertEqual(no_of_subsequences([-1, -2, -3], 2), 6)

    def test_zero_elements(self):
        self.assertEqual(no_of_subsequences([0], 1), 1)
        self.assertEqual(no_of_subsequences([0, 0], 1), 2)
        self.assertEqual(no_of_subsequences([0, 0], 2), 2)
