import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_simple_list(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3]), ([1, 2, 3], [2, 2, 2]))

    def test_edge_case_same_elements(self):
        self.assertEqual(count_duplic([1, 1, 1, 1, 1]), ([1], [5]))

    def test_edge_case_different_elements(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))

    def test_complex_case_mixed_elements(self):
        self.assertEqual(count_duplic([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), ([1, 2, 3, 4], [1, 2, 3, 4]))
