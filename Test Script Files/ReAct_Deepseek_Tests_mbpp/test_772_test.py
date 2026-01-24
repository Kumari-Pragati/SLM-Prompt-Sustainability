import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_length('Hello World', 5), 'Hello World')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_length('', 5), '')

    def test_edge_case_all_elements_of_length_K(self):
        self.assertEqual(remove_length('Hello Hello Hello', 5), '')

    def test_edge_case_no_elements_of_length_K(self):
        self.assertEqual(remove_length('Hello World', 7), 'Hello World')

    def test_edge_case_single_element_of_length_K(self):
        self.assertEqual(remove_length('Hello', 5), '')

    def test_edge_case_single_element_not_of_length_K(self):
        self.assertEqual(remove_length('Hello', 4), 'Hello')

    def test_edge_case_K_greater_than_all_elements(self):
        self.assertEqual(remove_length('Hello World', 10), '')
