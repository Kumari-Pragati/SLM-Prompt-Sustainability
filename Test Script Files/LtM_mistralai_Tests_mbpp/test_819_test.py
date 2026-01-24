import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_duplic([]), ([], []))
        self.assertEqual(count_duplic([1, 1, 2, 2, 3]), ([1, 2, 3], [2, 1, 1]))
        self.assertEqual(count_duplic([1, 1, 1, 2, 2, 3]), ([1, 2, 3], [3, 1, 1, 1]))

    def test_edge_cases(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))
        self.assertEqual(count_duplic([1, 1]), ([1], [2]))
        self.assertEqual(count_duplic([1, 1, 1]), ([1], [1]))
        self.assertEqual(count_duplic([1, 2, 2, 1]), ([1, 2], [1, 2]))
        self.assertEqual(count_duplic([1, 2, 2, 1, 1]), ([1, 2], [2, 1, 1]))

    def test_complex(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 1, 1]), ([1, 2], [2, 1, 2, 1]))
        self.assertEqual(count_duplic([1, 1, 1, 2, 2, 1, 1, 2]), ([1, 2, 1], [1, 3, 1, 1]))
        self.assertEqual(count_duplic([1, 2, 2, 1, 1, 2, 2]), ([1, 2, 1], [2, 2, 1]))
