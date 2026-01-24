import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        for num in range(10):
            self.assertEqual(max_occurrences([num]), num)

    def test_multiple_elements_same_value(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_multiple_elements_different_values(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1 or 2 or 3 or 4 or 5)

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -3]), -1)

    def test_zero(self):
        self.assertEqual(max_occurrences([0, 1, 2, 3]), 1)

    def test_large_numbers(self):
        self.assertEqual(max_occurrences([1000000001, 1000000001, 1000000002]), 1000000001)

    def test_duplicate_zero(self):
        self.assertEqual(max_occurrences([0, 0, 1]), 0)

    def test_large_numbers_with_zero(self):
        self.assertEqual(max_occurrences([0, 1000000001, 1000000001, 1000000002]), 1000000001)
