import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_equal_elements_list(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3]), 1)

    def test_multiple_max_elements(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_list_with_zero(self):
        self.assertEqual(max_occurrences([0, 1, 2]), 0)

    def test_list_with_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -3]), -1)

    def test_list_with_floats(self):
        self.assertEqual(max_occurrences([1.1, 2.2, 3.3]), 1.1)
