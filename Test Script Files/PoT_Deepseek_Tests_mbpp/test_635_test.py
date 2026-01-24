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
        self.assertEqual(heap_sort([3, 1, 2, 2]), [1, 2, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-1, -3, -2]), [-3, -2, -1])

    def test_large_numbers(self):
        self.assertEqual(heap_sort([100, 200, 150]), [100, 150, 200])

    def test_mixed_numbers(self):
        self.assertEqual(heap_sort([1, 2.5, 3, 2]), [1, 2, 2.5, 3])

    def test_non_integer_numbers(self):
        self.assertEqual(heap_sort([1.1, 2.2, 3.3, 2.2]), [1.1, 2.2, 2.2, 3.3])

    def test_string_elements(self):
        self.assertEqual(heap_sort(['b', 'a', 'c']), ['a', 'b', 'c'])
