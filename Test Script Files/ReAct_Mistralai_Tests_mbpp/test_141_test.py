import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_normal_list(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_reverse_list(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(pancake_sort([3, 3, 2, 1]), [1, 2, 3, 3])

    def test_large_list(self):
        large_list = [i for i in range(100)]
        self.assertEqual(pancake_sort(large_list), sorted(large_list))

    def test_negative_numbers(self):
        self.assertEqual(pancake_sort([-3, -2, -1]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(pancake_sort([-2, 0, 3, -1, 2]), [-1, 0, 2, 3, -2])

    def test_list_with_zero(self):
        self.assertEqual(pancake_sort([0]), [0])
