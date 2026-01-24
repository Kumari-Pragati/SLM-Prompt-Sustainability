import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertEqual(find_kth([], [], 0, 0, 1), 0)
        self.assertEqual(find_kth([], [], 1, 0, 1), 0)
        self.assertEqual(find_kth([], [], 0, 1, 1), 0)
        self.assertEqual(find_kth([], [], 1, 1, 1), 0)

    def test_single_element_arrays(self):
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)
        self.assertEqual(find_kth([1], [2], 1, 1, 1), 1)
        self.assertEqual(find_kth([2], [1], 1, 1, 1), 1)

    def test_equal_length_arrays(self):
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 1) , 3)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 2) , 4)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 3) , 5)

    def test_different_length_arrays(self):
        self.assertEqual(find_kth([1, 2, 3], [4, 5], 3, 2, 1) , 1)
        self.assertEqual(find_kth([1, 2, 3], [4, 5], 3, 2, 2) , 2)
        self.assertEqual(find_kth([1, 2, 3], [4, 5], 3, 2, 3) , 3)

    def test_k_greater_than_length(self):
        self.assertEqual(find_kth([1, 2, 3], [4, 5], 3, 2, 4) , 5)

    def test_k_less_than_1(self):
        self.assertEqual(find_kth([1, 2, 3], [4, 5], 3, 2, 0) , 0)

    def test_k_equal_1(self):
        self.assertEqual(find_kth([1, 2, 3], [4, 5], 3, 2, 1) , 1)
