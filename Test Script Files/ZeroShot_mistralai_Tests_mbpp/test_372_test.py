import unittest
from mbpp_372_code import List

from 372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(heap_assending([]), [])

    def test_single_element(self):
        self.assertListEqual(heap_assending([5]), [5])

    def test_multiple_elements(self):
        self.assertListEqual(heap_assending([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertListEqual(heap_assending([-5, -3, -1, -4, -2]), [-5, -3, -1, -2, -4])

    def test_duplicates(self):
        self.assertListEqual(heap_assending([1, 1, 2, 2, 3, 3, 4, 4, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5])
