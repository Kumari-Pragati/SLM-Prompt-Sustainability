import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 5, 8, 3, 6, 9, 2, 7, 4]
        n = 3
        expected = [8, 7, 6]
        self.assertListEqual(heap_queue_largest(nums, n), expected)

    def test_empty_list(self):
        nums = []
        n = 1
        self.assertListEqual(heap_queue_largest(nums, n), [])

    def test_single_element(self):
        nums = [1]
        n = 1
        expected = [1]
        self.assertListEqual(heap_queue_largest(nums, n), expected)

    def test_single_element_n_greater_than_list_size(self):
        nums = [1]
        n = 2
        self.assertListEqual(heap_queue_largest(nums, n), [1])

    def test_negative_numbers(self):
        nums = [-1, -5, -8, -3, -6, -9, -2, -7, -4]
        n = 3
        expected = [-8, -7, -6]
        self.assertListEqual(heap_queue_largest(nums, n), expected)

    def test_floats(self):
        nums = [1.1, 5.5, 8.8, 3.3, 6.6, 9.9, 2.2, 7.7, 4.4]
        n = 3
        expected = [9.9, 8.8, 7.7]
        self.assertListEqual(heap_queue_largest(nums, n), expected)

    def test_duplicates(self):
        nums = [1, 1, 5, 8, 3, 6, 9, 2, 7, 4]
        n = 3
        expected = [8, 7, 6]
        self.assertListEqual(heap_queue_largest(nums, n), expected)
