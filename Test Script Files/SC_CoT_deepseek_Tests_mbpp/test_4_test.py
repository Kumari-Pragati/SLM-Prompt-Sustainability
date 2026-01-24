import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 4), [9, 6, 5, 5])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 0), [])

    def test_edge_case_n_equals_len_of_nums(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 10), [9, 6, 5, 5, 4, 3, 3, 2, 1, 1])

    def test_edge_case_n_greater_than_len_of_nums(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 11), [9, 6, 5, 5, 4, 3, 3, 2, 1, 1, 1])

    def test_special_case_negative_numbers(self):
        self.assertEqual(heap_queue_largest([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3], 4), [-1, -2, -3, -4])

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], -1)

    def test_invalid_input_n_greater_than_len_of_nums(self):
        with self.assertRaises(ValueError):
            heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 11)
