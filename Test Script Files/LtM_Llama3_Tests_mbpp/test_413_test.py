import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 1), [1, 4])

    def test_empty_input(self):
        self.assertEqual(extract_nth_element([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(extract_nth_element([[1, 2, 3]], 1), [1])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_nth_element([1, 2, 3], 'a')

    def test_invalid_n_value(self):
        with self.assertRaises(IndexError):
            extract_nth_element([[1, 2, 3]], 5)

    def test_multiple_lists(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [1, 4, 7])

    def test_list_with_single_element(self):
        self.assertEqual(extract_nth_element([[1]], 0), [1])
