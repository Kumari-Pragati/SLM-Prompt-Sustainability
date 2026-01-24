import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_empty_input(self):
        self.assertRaises(IndexError, find_kth, [], [], 0, 0, 0)

    def test_single_array(self):
        self.assertEqual(find_kth([1, 2, 3], [], 3, 0, 1), 1)

    def test_single_array2(self):
        self.assertEqual(find_kth([], [1, 2, 3], 0, 3, 1), 1)

    def test_k_out_of_range(self):
        self.assertRaises(IndexError, find_kth, [1, 2, 3], [], 3, 0, 4)

    def test_kth_element(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [], 5, 0, 3), 3)

    def test_kth_element2(self):
        self.assertEqual(find_kth([], [1, 2, 3, 4, 5], 0, 5, 3), 3)

    def test_kth_element3(self):
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 2), 5)

    def test_kth_element4(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 4), 8)
