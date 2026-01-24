import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 3), 5)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 2), 3)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)

    def test_edge_case_1(self):
        self.assertEqual(find_kth([1], [1], 1, 1, k) for k in range(1, 2))

    def test_edge_case_2(self):
        self.assertEqual(find_kth([1], [], 1, 0, k) for k in range(1, 0, -1))

    def test_edge_case_3(self):
        self.assertEqual(find_kth([], [1], 0, 1, k) for k in range(1, 0, -1))

    def test_invalid_input_1(self):
        self.assertRaises(TypeError, find_kth, [1], [2], 2, 2, 'k')

    def test_invalid_input_2(self):
        self.assertRaises(TypeError, find_kth, [1], [2], -1, 2, k)

    def test_invalid_input_3(self):
        self.assertRaises(TypeError, find_kth, [1], [2], 2, -1, k)
