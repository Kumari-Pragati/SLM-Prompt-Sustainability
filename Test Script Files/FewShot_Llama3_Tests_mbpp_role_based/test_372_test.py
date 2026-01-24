import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_assending([5]), [5])

    def test_multiple_elements_list(self):
        self.assertEqual(heap_assending([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(heap_assending([3, 1, 4, 1, 5, 9, 2, 6, 6]), [1, 1, 2, 3, 4, 5, 6, 6, 9])

    def test_list_with_negative_numbers(self):
        self.assertEqual(heap_assending([-5, -2, -1, 0, 1, 2, 3, 4, 5]), [-5, -2, -1, 0, 1, 2, 3, 4, 5])
