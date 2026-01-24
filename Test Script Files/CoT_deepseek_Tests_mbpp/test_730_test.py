import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_single_element(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_all_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 1, 1]), [1])

    def test_no_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 3]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(consecutive_duplicates([-1, -1, -2, -2]), [-1, -2])

    def test_mixed_numbers(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 3, 1]), [1, 2, 3, 1])
