import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 2, 4, 4, 1], 8), 1)
        self.assertEqual(get_odd_occurence([4, 4, 4, 4, 4, 4, 4, 4, 1], 9), 1)
        self.assertEqual(get_odd_occurence([20, 1, -1, 1, 20, 20, -1, -1, 20], 9), -1)

    def test_edge_input(self):
        self.assertEqual(get_odd_occurence([], 0), -1)
        self.assertEqual(get_odd_occurence([1], 1), 1)
        self.assertEqual(get_odd_occurence([1, 1], 2), -1)
        self.assertEqual(get_odd_occurence([1, 1, 1], 3), 1)

    def test_boundary_input(self):
        self.assertEqual(get_odd_occurence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 0)
        self.assertEqual(get_odd_occurence([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], 10), 9)
        self.assertEqual(get_odd_occurence([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 10)
