import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(frequency([1, 2, 3, 2, 4, 2, 5], 2), 3)

    def test_empty_list(self):
        self.assertEqual(frequency([], 1), 0)

    def test_list_with_no_occurrences(self):
        self.assertEqual(frequency([1, 3, 5, 7], 4), 0)

    def test_list_with_single_occurrence(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 3), 1)

    def test_list_with_multiple_occurrences(self):
        self.assertEqual(frequency([1, 2, 2, 3, 3, 3, 4, 5, 5, 5], 3), 3)

    def test_list_with_non_integer_elements(self):
        self.assertEqual(frequency(['a', 'b', 'c', 'a', 'b', 'c'], 'a'), 2)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            frequency(123, 1)
