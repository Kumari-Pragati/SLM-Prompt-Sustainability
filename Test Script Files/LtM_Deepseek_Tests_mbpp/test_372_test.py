import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(heap_assending([3, 1, 2]), [1, 2, 3])

    def test_empty_input(self):
        self.assertEqual(heap_assending([]), [])

    def test_single_element_input(self):
        self.assertEqual(heap_assending([5]), [5])

    def test_duplicate_elements_input(self):
        self.assertEqual(heap_assending([3, 1, 2, 2, 3]), [1, 2, 2, 3, 3])

    def test_negative_numbers_input(self):
        self.assertEqual(heap_assending([-3, -1, -2]), [-3, -2, -1])

    def test_large_numbers_input(self):
        self.assertEqual(heap_assending([1000, 2000, 500, 3000]), [500, 1000, 2000, 3000])
