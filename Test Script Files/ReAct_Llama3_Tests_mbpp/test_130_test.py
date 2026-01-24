import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_multiple_elements_list(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3]), (3, 3))

    def test_no_duplicates(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), (1, 1))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -2, -3, -3, -3]), (-3, 3))

    def test_mixed_numbers(self):
        self.assertEqual(max_occurrences([1, -2, 2, 3, -3, 3]), (3, 2))
