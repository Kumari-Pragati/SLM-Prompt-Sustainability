import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, extract_nth_element, [], 0)

    def test_single_element_list(self):
        self.assertEqual(extract_nth_element([1], 0), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(extract_nth_element([1, 2, 3], 1), [2])

    def test_negative_index(self):
        self.assertRaises(IndexError, extract_nth_element, [1, 2, 3], -1)

    def test_index_greater_than_length(self):
        self.assertRaises(IndexError, extract_nth_element, [1, 2, 3], 3)

    def test_list_with_non_integer_elements(self):
        self.assertRaises(TypeError, extract_nth_element, [1, 'a', 3], 1)

    def test_list_with_non_list_elements(self):
        self.assertRaises(TypeError, extract_nth_element, [1, [2, 3]], 1)
