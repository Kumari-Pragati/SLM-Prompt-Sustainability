import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_duplicate_elements_list(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3, 3, 3]), 3)

    def test_negative_numbers_list(self):
        self.assertEqual(max_occurrences([-1, -1, 0, 0, 1]), -1)

    def test_list_with_same_max_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3]), 2)
