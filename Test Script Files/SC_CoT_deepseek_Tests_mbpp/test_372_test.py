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
        nums = [1]
        self.assertEqual(heap_assending(nums), [1])

    def test_negative_numbers(self):
        nums = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        self.assertEqual(heap_assending(nums), sorted(nums))

    def test_duplicate_elements(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(heap_assending(nums), sorted(nums))

    def test_large_numbers(self):
        nums = [1000000, 999999, 1000001, 999998, 1000002]
        self.assertEqual(heap_assending(nums), sorted(nums))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_assending(None)
