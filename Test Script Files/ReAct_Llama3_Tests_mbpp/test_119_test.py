import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):
    def test_search_single_element(self):
        self.assertEqual(search([1], 1), 1)

    def test_search_multiple_elements(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)

    def test_search_all_elements_equal(self):
        self.assertEqual(search([1, 1, 1, 1, 1], 5), 0)

    def test_search_all_elements_zero(self):
        self.assertEqual(search([0, 0, 0, 0, 0], 5), 0)

    def test_search_empty_array(self):
        with self.assertRaises(IndexError):
            search([], 0)

    def test_search_invalid_input_type(self):
        with self.assertRaises(TypeError):
            search("hello", 0)

    def test_search_invalid_input_length(self):
        with self.assertRaises(TypeError):
            search([1, 2, 3], "hello")
