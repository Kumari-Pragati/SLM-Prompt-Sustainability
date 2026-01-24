import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_kth([1, 3, 5, 7], [2, 4, 6, 8], 4, 4, 3), 5)

    def test_edge_cases(self):
        self.assertEqual(find_kth([1, 2, 3], [], 3, 0, 1), 1)
        self.assertEqual(find_kth([], [1, 2, 3], 0, 3, 1), 1)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 3), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(IndexError):
            find_kth([1, 2, 3], [4, 5, 6], 3, 2, 4)
        with self.assertRaises(IndexError):
            find_kth([1, 2, 3], [4, 5, 6], 2, 3, 4)

    def test_k_out_of_range(self):
        with self.assertRaises(IndexError):
            find_kth([1, 2, 3], [4, 5, 6], 3, 3, 7)
