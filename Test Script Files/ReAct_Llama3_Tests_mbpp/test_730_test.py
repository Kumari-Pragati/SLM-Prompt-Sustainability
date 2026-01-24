import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_no_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
