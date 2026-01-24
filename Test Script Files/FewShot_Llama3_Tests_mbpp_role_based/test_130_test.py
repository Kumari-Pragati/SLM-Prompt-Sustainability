import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(max_occurrences([1, 2, 3]), (3, 1))

    def test_multiple_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_all_occurrences_equal(self):
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2]), (2, 3))

    def test_empty_list(self):
        self.assertRaises(TypeError, max_occurrences, [])

    def test_non_integer_values(self):
        self.assertRaises(TypeError, max_occurrences, [1, 2, 'a', 3])
