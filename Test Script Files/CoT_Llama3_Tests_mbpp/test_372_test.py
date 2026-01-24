import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_heap_assending_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_heap_assending_single_element_list(self):
        self.assertEqual(heap_assending([5]), [5])

    def test_heap_assending_multiple_elements_list(self):
        self.assertEqual(heap_assending([5, 2, 8, 3, 1]), [1, 2, 3, 5, 8])

    def test_heap_assending_negative_numbers(self):
        self.assertEqual(heap_assending([-5, -2, -8, -3, -1]), [-8, -5, -3, -2, -1])

    def test_heap_assending_duplicates(self):
        self.assertEqual(heap_assending([5, 2, 8, 3, 1, 5]), [1, 2, 3, 5, 5, 8])

    def test_heap_assending_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            heap_assending([5, 2, 8, 3, 1, 'a'])
