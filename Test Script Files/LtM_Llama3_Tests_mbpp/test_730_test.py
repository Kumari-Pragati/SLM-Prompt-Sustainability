import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_single_element_input(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_single_duplicate_input(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 3]), [1, 2, 3])

    def test_multiple_duplicates_input(self):
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_consecutive_duplicates_input(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])

    def test_non_consecutive_duplicates_input(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 5, 5, 6]), [1, 2, 3, 4, 5, 6])
