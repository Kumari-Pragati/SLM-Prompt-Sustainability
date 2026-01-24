import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_assending([3, 5, 1, 7, 2]), [1, 2, 3, 5, 7])
        self.assertEqual(heap_assending([-3, -5, -1, -7, -2]), [-3, -5, -7, -2, -1])
        self.assertEqual(heap_assending([0]), [0])
        self.assertEqual(heap_assending([1]), [1])
        self.assertEqual(heap_assending([1, 1]), [1, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(heap_assending([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(heap_assending([0]), [0])

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(heap_assending([1, 1, 2, 1, 2]), [1, 1, 2, 2])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(heap_assending([-1, -2, -3]), [-3, -2, -1])
