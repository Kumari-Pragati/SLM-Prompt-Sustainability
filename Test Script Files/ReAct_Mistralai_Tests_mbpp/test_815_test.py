import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDNF(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_sort_single_element(self):
        for value in [0, 1, 2]:
            self.assertEqual(sort_by_dnf([value], 1), [value])

    def test_sort_two_elements(self):
        for arr in [
            [0, 1],
            [1, 0],
            [1, 2],
            [2, 1],
            [2, 0],
            [0, 2]
        ]:
            self.assertEqual(sort_by_dnf(arr, len(arr)), arr.sort())

    def test_sort_multiple_elements(self):
        for arr in [
            [0, 1, 2],
            [2, 1, 0],
            [2, 0, 1],
            [1, 2, 0],
            [1, 0, 2],
            [0, 2, 1]
        ]:
            self.assertEqual(sort_by_dnf(arr, len(arr)), arr.sort())

    def test_sort_with_duplicates(self):
        for arr in [
            [0, 0, 1, 2],
            [2, 1, 0, 0],
            [2, 0, 1, 0],
            [1, 2, 0, 0],
            [1, 0, 2, 0],
            [0, 2, 1, 0],
            [0, 1, 2, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 0]
        ]:
            self.assertEqual(sort_by_dnf(arr, len(arr)), arr.sort())

    def test_sort_with_large_numbers(self):
        for arr in [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [9, 0, 8, 1, 7, 2, 6, 3, 4, 5]
        ]:
            self.assertEqual(sort_by_dnf(arr, len(arr)), arr.sort())
