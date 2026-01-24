import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), (5, 1))

    def test_multiple_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), (5, 2))

    def test_all_occurrences_equal(self):
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), (5, 3))

    def test_empty_input(self):
        self.assertRaises(TypeError, max_occurrences, [])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            max_occurrences(['a', 'b', 'c'])
