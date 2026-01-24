import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):
    def test_consecutive_duplicates_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_consecutive_duplicates_single_element(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_consecutive_duplicates_single_duplicate(self):
        self.assertEqual(consecutive_duplicates([1, 1]), [1])

    def test_consecutive_duplicates_multiple_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_consecutive_duplicates_increasing_sequence(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 3])

    def test_consecutive_duplicates_decreasing_sequence(self):
        self.assertEqual(consecutive_duplicates([5, 4, 4, 3, 3]), [5, 4])

    def test_consecutive_duplicates_duplicate_at_beginning(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_consecutive_duplicates_duplicate_at_end(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3]), [1, 2])
