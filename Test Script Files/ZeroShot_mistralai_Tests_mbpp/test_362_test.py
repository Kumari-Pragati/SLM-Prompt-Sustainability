import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_multiple_elements_equal_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), 1 or 2 or 3)

    def test_multiple_elements_different_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 4]), 2 or 3)

    def test_max_occurrences_with_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -2, -3, -3]), -2)

    def test_max_occurrences_with_zero(self):
        self.assertEqual(max_occurrences([0, 1, 2, 3, 0]), 0)
