import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 5), 5)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 2), 3)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(find_kth([1], [1], 1, 1, 1), 1)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)
        self.assertEqual(find_kth([], [], 0, 0, 1), 0)

    def test_corner_cases(self):
        self.assertEqual(find_kth([1], [1], 1, 1, 2), 1)
        self.assertEqual(find_kth([1], [1], 1, 1, 0), TraceError)
        self.assertEqual(find_kth([], [], 0, 0, 2), TraceError)
