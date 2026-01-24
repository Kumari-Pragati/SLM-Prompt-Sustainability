import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(heap_assending([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_assending([1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(heap_assending([-5, -3, -1, -4, -2]), [-5, -4, -3, -2, -1])

    def test_duplicates(self):
        self.assertEqual(heap_assending([1, 1, 2, 2, 3]), [1, 1, 2, 2, 3])
