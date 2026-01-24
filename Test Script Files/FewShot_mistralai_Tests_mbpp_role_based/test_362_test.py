import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3]), 2)

    def test_equal_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3]), 2)

    def test_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, 0, 0, 1]), -1)

    def test_zero(self):
        self.assertEqual(max_occurrences([0, 0, 1]), 0)
