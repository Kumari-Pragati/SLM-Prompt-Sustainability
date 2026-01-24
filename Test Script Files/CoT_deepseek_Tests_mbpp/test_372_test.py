import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_typical_case(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(heap_assending(nums), sorted(nums))

    def test_empty_list(self):
        nums = []
        self.assertEqual(heap_assending(nums), [])

    def test_single_element(self):
        nums = [7]
        self.assertEqual(heap_assending(nums), [7])

    def test_duplicate_elements(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(heap_assending(nums), [1, 1, 1, 1, 1])

    def test_negative_numbers(self):
        nums = [-1, -3, -5, -2, -4]
        self.assertEqual(heap_assending(nums), sorted(nums))

    def test_mixed_numbers(self):
        nums = [-1, 3, -5, 2, -4]
        self.assertEqual(heap_assending(nums), sorted(nums))
