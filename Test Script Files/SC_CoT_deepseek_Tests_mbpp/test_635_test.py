import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(heap_sort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-5, -3, -1, 0, 2]), [-5, -3, -1, 0, 2])

    def test_large_numbers(self):
        self.assertEqual(heap_sort([100, 200, 300, 400]), [100, 200, 300, 400])

    def test_mixed_numbers(self):
        self.assertEqual(heap_sort([10, 20, -30, 40, -50]), [-50, -30, 10, 20, 40])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            heap_sort([1, 2, 'three', 4])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            heap_sort('not a list')
