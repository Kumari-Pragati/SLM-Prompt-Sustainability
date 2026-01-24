import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), (None, 0))

    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_multiple_elements_same_max(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), (1, 2))

    def test_multiple_elements_different_max(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 4]), (3, 3))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -2, -3]), (-2, 2))

    def test_large_numbers(self):
        self.assertEqual(max_occurrences([1000000001, 1000000001, 1000000002]), (1000000001, 2))

    def test_zero(self):
        self.assertEqual(max_occurrences([0, 1, 1, 2, 2, 3]), (1, 2))
