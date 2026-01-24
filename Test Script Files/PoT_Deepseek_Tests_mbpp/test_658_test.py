import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_all_same_elements(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_occurrences([1, -1, -1, 2, 2]), 2)

    def test_large_numbers(self):
        self.assertEqual(max_occurrences([1000, 2000, 2000]), 2000)
