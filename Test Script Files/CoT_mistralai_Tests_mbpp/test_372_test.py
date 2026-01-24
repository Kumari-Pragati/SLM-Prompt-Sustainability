import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], heap_assending([]))

    def test_single_element(self):
        self.assertListEqual([1], heap_assending([1]))

    def test_multiple_elements(self):
        self.assertListEqual([1, 2, 3, 4, 5], heap_assending([5, 3, 4, 1, 2]))

    def test_duplicates(self):
        self.assertListEqual([1, 1, 2, 3], heap_assending([3, 1, 1, 2]))

    def test_negative_numbers(self):
        self.assertListEqual([-5, -4, -3, -2, -1], heap_assending([-5, -3, -2, -1, -4]))

    def test_large_numbers(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heap_assending(list(range(1, 11))))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_assending(1.23)
