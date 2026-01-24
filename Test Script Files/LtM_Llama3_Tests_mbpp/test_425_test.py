import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(count_element_in_list([1, 2, 3], 2), 1)

    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 2), 0)

    def test_list_with_no_occurrences(self):
        self.assertEqual(count_element_in_list([1, 3, 4], 2), 0)

    def test_list_with_multiple_occurrences(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3], 2), 2)

    def test_list_with_non_integer_elements(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c'], 'a'), 1)

    def test_list_with_non_list_input(self):
        with self.assertRaises(TypeError):
            count_element_in_list(123, 'a')

    def test_list_with_non_integer_search_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3], 'a'), 0)
