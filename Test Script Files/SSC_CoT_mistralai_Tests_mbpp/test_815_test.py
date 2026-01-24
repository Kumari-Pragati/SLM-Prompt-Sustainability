import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_sort_normal(self):
        arr = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
        expected = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected)

    def test_sort_empty(self):
        arr = []
        self.assertEqual(sort_by_dnf(arr, len(arr)), arr)

    def test_sort_single_element(self):
        arr = [0]
        expected = [0]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected)

    def test_sort_all_zeros(self):
        arr = [0] * 10
        expected = [0] * 10
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected)

    def test_sort_all_ones(self):
        arr = [1] * 10
        expected = [1] * 10
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected)

    def test_sort_mixed_zeros_and_ones(self):
        arr = [0, 1, 0, 1, 0, 1, 0, 1]
        expected = [0, 0, 0, 0, 1, 1, 1, 1]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected)

    def test_sort_invalid_input(self):
        with self.assertRaises(ValueError):
            sort_by_dnf('invalid', 5)
