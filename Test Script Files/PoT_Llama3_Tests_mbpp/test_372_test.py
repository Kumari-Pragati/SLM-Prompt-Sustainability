import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_assending([5, 2, 8, 3, 1, 4, 6, 7]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_edge_case_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(heap_assending([5]), [5])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(heap_assending([-5, -2, -8, -3, -1, -4, -6, -7]), [-8, -7, -6, -5, -4, -3, -2, -1])

    def test_edge_case_duplicates(self):
        self.assertEqual(heap_assending([5, 2, 8, 3, 1, 4, 6, 7, 5, 2, 8, 3, 1, 4, 6, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8])
