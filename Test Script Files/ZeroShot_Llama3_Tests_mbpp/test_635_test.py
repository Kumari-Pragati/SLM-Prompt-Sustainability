import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(heap_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(heap_sort([5, 2, 8, 2, 1, 9]), [1, 2, 2, 5, 8, 9])

    def test_large_list(self):
        import random
        lst = [random.randint(0, 1000) for _ in range(100)]
        self.assertEqual(heap_sort(lst), sorted(lst))
