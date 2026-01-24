import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([4]), [4])

    def test_multiple_elements(self):
        self.assertEqual(heap_sort([5, 3, 1, 4, 6]), [1, 3, 4, 5, 6])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-5, -3, -1, 0, 4]), [-5, -3, -1, 0, 4])

    def test_floats(self):
        self.assertAlmostEqual(heap_sort([3.14, 2.71, 1.618]), [1.618, 2.71, 3.14])

    def test_duplicates(self):
        self.assertEqual(heap_sort([3, 3, 1, 3, 4]), [1, 3, 3, 3, 4])

    def test_large_list(self):
        large_list = [i for i in range(100)]
        sorted_list = sorted(large_list)
        self.assertEqual(heap_sort(large_list), sorted_list)

    def test_list_with_none(self):
        self.assertEqual(heap_sort([None, 3, 1, 4, None]), [1, 3, 4, None, None])

    def test_list_with_string(self):
        self.assertEqual(heap_sort(['b', 'a', 'c']), ['a', 'b', 'c'])
