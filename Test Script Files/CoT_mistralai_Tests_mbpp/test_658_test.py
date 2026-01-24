import unittest
from mbpp_658_code import Counter
from 658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        for element in [1, 'a', 3.14]:
            self.assertEqual(max_occurrences([element]), element)

    def test_multiple_elements_same_occurrences(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_multiple_elements_different_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 4]), 2)

    def test_list_with_zero(self):
        self.assertEqual(max_occurrences([0, 1, 2, 0, 3]), 0)

    def test_list_with_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -3]), -1)

    def test_list_with_floats(self):
        self.assertEqual(max_occurrences([1.1, 2.2, 3.3]), 2.2)

    def test_list_with_strings(self):
        self.assertEqual(max_occurrences(['a', 'b', 'a', 'c']), 'a')

    def test_list_with_duplicate_strings(self):
        self.assertEqual(max_occurrences(['a', 'a', 'b', 'a']), 'a')

    def test_list_with_empty_strings(self):
        self.assertEqual(max_occurrences(['', 'a', 'b']), '')

    def test_list_with_lists(self):
        self.assertEqual(max_occurrences([[1], [1], [2], [2], [3]]), [1])

    def test_list_with_nested_lists(self):
        self.assertEqual(max_occurrences([[1], [1, 1], [2], [2, 2], [3]]), [1, 1])

    def test_list_with_invalid_input(self):
        self.assertRaises(TypeError, max_occurrences, [1, 2, '3'])
