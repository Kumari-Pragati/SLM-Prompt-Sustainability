import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([4]), [4])

    def test_multiple_elements(self):
        self.assertEqual(heap_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(heap_sort([3, 3, 1, 2, 2, 5, 5]), [1, 2, 3, 3, 5, 5])

    def test_large_list(self):
        self.assertEqual(heap_sort(list(range(100))), list(range(100)))

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-5, -3, -1, 0, 2]), [-5, -3, -1, 0, 2])

    def test_floats(self):
        self.assertEqual(heap_sort([3.14, 2.71, 1.618]), [1.618, 2.71, 3.14])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_sort('string')
