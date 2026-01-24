import unittest
from mbpp_730_code import (chain, islice, repeat)
from 730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4]), [1, 1, 2, 2, 3, 3, 4])
        self.assertListEqual(consecutive_duplicates([1, 1, 1, 2, 2, 3, 3, 4]), [1, 1, 1, 2, 2, 3, 3, 4])
        self.assertListEqual(consecutive_duplicates([1, 1, 1, 1, 2, 2, 3, 3, 4]), [1, 1, 1, 1, 2, 2, 3, 3, 4])

    def test_edge_cases(self):
        self.assertListEqual(consecutive_duplicates([]), [])
        self.assertListEqual(consecutive_duplicates([1]), [1])
        self.assertListEqual(consecutive_duplicates([1, 1]), [1, 1])
        self.assertListEqual(consecutive_duplicates([1, 2, 1]), [1, 2, 1])
        self.assertListEqual(consecutive_duplicates([1, 1, 2]), [1, 1, 2])
        self.assertListEqual(consecutive_duplicates([1, 1, 1, 2]), [1, 1, 1, 2])
        self.assertListEqual(consecutive_duplicates([1, 1, 1, 1, 2]), [1, 1, 1, 1, 2])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, consecutive_duplicates, (1, 2, 3))
        self.assertRaises(TypeError, consecutive_duplicates, ['1', '2', '3'])
