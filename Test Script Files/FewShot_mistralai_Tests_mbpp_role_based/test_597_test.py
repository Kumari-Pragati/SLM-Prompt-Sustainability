import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 3), 5)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 8), 10)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 1), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_kth([], [], 0, 0, 1), None)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([1], [2], 1, 1, 1), 1)
        self.assertEqual(find_kth([1], [2], 1, 1, 2), 2)
        self.assertEqual(find_kth([1], [2], 1, 1, 0), None)
