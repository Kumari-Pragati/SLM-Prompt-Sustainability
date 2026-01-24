import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        for element in [1, 'a', 3.14]:
            self.assertEqual(max_occurrences([element]), element)

    def test_multiple_elements_same_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_multiple_elements_different_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3]), 2)

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, 0, 1]), -1)

    def test_floats(self):
        self.assertEqual(max_occurrences([3.14, 3.14, 2.71, 2.71]), 3.14)

    def test_strings(self):
        self.assertEqual(max_occurrences(['a', 'a', 'b', 'b', 'c']), 'a')

    def test_list_with_none(self):
        self.assertEqual(max_occurrences([None, None, 1, 1, 2]), None)
