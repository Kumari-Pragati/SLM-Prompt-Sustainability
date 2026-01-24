import unittest
from mbpp_730_code import (chain, islice)
from 730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(consecutive_duplicates([]), [])

    def test_single_element(self):
        self.assertListEqual(consecutive_duplicates([1]), [1])

    def test_consecutive_duplicates(self):
        self.assertListEqual(consecutive_duplicates([1, 1, 2, 1, 2, 3, 2, 2]), [1, 2, 3, 2])

    def test_consecutive_duplicates_with_gaps(self):
        self.assertListEqual(consecutive_duplicates([1, 2, 1, 3, 1, 4, 1, 5]), [1, 2, 1, 3, 1])

    def test_consecutive_duplicates_with_repeated_values(self):
        self.assertListEqual(consecutive_duplicates([1, 1, 1, 2, 1, 1, 2]), [1, 2])

    def test_consecutive_duplicates_with_non_consecutive_duplicates(self):
        self.assertListEqual(consecutive_duplicates([1, 2, 1, 2, 1, 2, 1]), [1, 2])

    def test_consecutive_duplicates_with_non_numeric_input(self):
        self.assertRaises(TypeError, consecutive_duplicates, ['a', 'b', 'a'])

    def test_consecutive_duplicates_with_mixed_types(self):
        self.assertRaises(TypeError, consecutive_duplicates, [1, 'a', 2, 'a', 1])
