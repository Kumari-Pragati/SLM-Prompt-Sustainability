import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(heap_sort([4, 2, 7, 1, 3]), [1, 2, 3, 4, 7])

    def test_empty_input(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_input(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_negative_numbers_input(self):
        self.assertEqual(heap_sort([-5, 2, -3, 1]), [-5, -3, 1, 2])

    def test_duplicates_input(self):
        self.assertEqual(heap_sort([5, 2, 5, 1, 3]), [1, 2, 3, 5, 5])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            heap_sort(['a', 'b', 'c'])

    def test_mixed_input(self):
        self.assertEqual(heap_sort([4, 2, 'a', 7, 1, 3]), [1, 2, 3, 4, 7])

    def test_large_input(self):
        import random
        large_list = [random.randint(1, 100) for _ in range(100)]
        self.assertEqual(heap_sort(large_list), sorted(large_list))
