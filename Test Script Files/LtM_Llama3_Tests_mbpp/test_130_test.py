import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_input(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_multiple_elements_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_duplicates_input(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3, 3]), (3, 3))

    def test_max_occurrences_at_start(self):
        self.assertEqual(max_occurrences([3, 3, 3, 2, 2, 1]), (3, 3))

    def test_max_occurrences_at_end(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 3]), (3, 3))

    def test_max_occurrences_at_middle(self):
        self.assertEqual(max_occurrences([1, 2, 3, 3, 3, 2, 2, 1]), (3, 3))

    def test_max_occurrences_at_start_and_end(self):
        self.assertEqual(max_occurrences([3, 3, 1, 2, 2, 3, 3, 3]), (3, 3))

    def test_max_occurrences_at_start_and_middle(self):
        self.assertEqual(max_occurrences([3, 3, 2, 2, 1, 2, 2, 3, 3]), (3, 3))

    def test_max_occurrences_at_end_and_middle(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 3, 2, 2]), (3, 3))

    def test_max_occurrences_at_start_and_middle_and_end(self):
        self.assertEqual(max_occurrences([3, 3, 2, 2, 1, 2, 2, 3, 3, 3]), (3, 3))
