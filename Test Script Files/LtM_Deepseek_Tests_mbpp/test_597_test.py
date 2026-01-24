import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 3), 4)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 5), 5)

    def test_edge_conditions(self):
        self.assertEqual(find_kth([], [1, 2, 3], 0, 3, 2), 2)
        self.assertEqual(find_kth([1, 2, 3], [], 3, 0, 2), 2)
        self.assertEqual(find_kth([], [], 0, 0, 1), None)

    def test_boundary_conditions(self):
        self.assertEqual(find_kth([1], [2], 1, 1, 1), 1)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 1), 1)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 7), 3)

    def test_complex_cases(self):
        self.assertEqual(find_kth([10, 20, 30], [5, 15, 25], 3, 3, 5), 15)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 10), 10)
