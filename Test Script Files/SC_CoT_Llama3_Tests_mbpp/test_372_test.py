import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_typical_input(self):
        nums = [5, 3, 8, 6, 2, 4]
        result = heap_assending(nums)
        self.assertEqual(result, [2, 3, 4, 5, 6, 8])

    def test_empty_input(self):
        nums = []
        result = heap_assending(nums)
        self.assertEqual(result, [])

    def test_single_element_input(self):
        nums = [5]
        result = heap_assending(nums)
        self.assertEqual(result, [5])

    def test_negative_numbers_input(self):
        nums = [-5, 3, -8, 6, -2, 4]
        result = heap_assending(nums)
        self.assertEqual(result, [-8, -5, -2, 3, 4, 6])

    def test_duplicates_input(self):
        nums = [5, 3, 8, 6, 2, 4, 5, 3]
        result = heap_assending(nums)
        self.assertEqual(result, [2, 3, 3, 4, 5, 5, 6, 8])

    def test_invalid_input_type(self):
        nums = 'abc'
        with self.assertRaises(TypeError):
            heap_assending(nums)

    def test_invalid_input_structure(self):
        nums = [[1, 2], [3, 4]]
        with self.assertRaises(TypeError):
            heap_assending(nums)
