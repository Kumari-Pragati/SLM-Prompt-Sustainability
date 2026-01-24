import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_sort([3, 1, 2]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(heap_sort([3, 1, 2, 2, 1, 3]), [1, 1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-3, -1, -2]), [-3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(heap_sort([3, -1, 2]), [-1, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(heap_sort([100, 200, 300, 250]), [100, 200, 250, 300])

    def test_float_numbers(self):
        self.assertEqual(heap_sort([1.1, 1.2, 1.3]), [1.1, 1.2, 1.3])

    def test_string_elements(self):
        with self.assertRaises(TypeError):
            heap_sort(['a', 'b', 'c'])

    def test_non_comparable_elements(self):
        with self.assertRaises(TypeError):
            heap_sort([[1, 2], [3, 4]])
