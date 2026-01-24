import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_assending([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(heap_assending([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(heap_assending([5, 2, 8, 3, 1, 4]), [1, 2, 3, 4, 5, 8])

    def test_duplicates(self):
        self.assertEqual(heap_assending([1, 2, 2, 3, 3, 3, 4, 5, 5]), [1, 2, 2, 3, 3, 3, 4, 5, 5])

    def test_negative_numbers(self):
        self.assertEqual(heap_assending([-5, -2, 0, 1, 3, 4]), [-5, -2, 0, 1, 3, 4])
