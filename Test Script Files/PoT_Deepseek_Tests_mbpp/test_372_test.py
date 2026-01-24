import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_assending([3, 1, 2]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_single_element(self):
        self.assertEqual(heap_assending([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(heap_assending([3, 1, 2, 1]), [1, 1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(heap_assending([-3, -1, -2]), [-3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(heap_assending([3, -1, 2]), [-1, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(heap_assending([100, 200, 300]), [100, 200, 300])

    def test_large_and_small_numbers(self):
        self.assertEqual(heap_assending([-100, 200, -300]), [-300, -100, 200])
