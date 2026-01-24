import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9], 5, 5, 3), 5)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 2), 3)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(find_kth([1], [2], 1, 1, 1), 1)
        self.assertEqual(find_kth([1, 2], [], 2, 0, 1), 1)
        self.assertEqual(find_kth([], [1, 2], 0, 2, 1), 1)
        self.assertEqual(find_kth([1, 2], [1, 2], 2, 2, 2), 2)

    def test_complex(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 6, 6), 10)
        self.assertEqual(find_kth([10, 9, 8, 7, 6], [5, 4, 3, 2, 1], 5, 5, 1), 1)
        self.assertEqual(find_kth([10, 9, 8, 7, 6], [5, 4, 3, 2, 1], 6, 5, 6), 10)
