import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove(['hello123', 'world456']), ['hello', 'world'])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(remove(['hello']), ['hello'])

    def test_edge_case_list_of_empty_strings(self):
        self.assertEqual(remove(['', '', '']), ['', '', ''])

    def test_edge_case_list_of_strings_without_numbers(self):
        self.assertEqual(remove(['hello', 'world']), ['hello', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings(self):
        self.assertEqual(remove(['hello123', '', 'world456']), ['hello', '', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings_and_duplicates(self):
        self.assertEqual(remove(['hello123', '', 'world456', 'hello789', '', 'world']), ['hello', '', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings_and_duplicates_and_duplicates(self):
        self.assertEqual(remove(['hello123', '', 'world456', 'hello789', '', 'world', 'hello123']), ['hello', '', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(remove(['hello123', '', 'world456', 'hello789', '', 'world', 'hello123', 'hello123']), ['hello', '', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(remove(['hello123', '', 'world456', 'hello789', '', 'world', 'hello123', 'hello123', 'hello123']), ['hello', '', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(remove(['hello123', '', 'world456', 'hello789', '', 'world', 'hello123', 'hello123', 'hello123', 'hello123']), ['hello', '', 'world'])

    def test_edge_case_list_of_strings_with_numbers_and_empty_strings_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(remove(['hello123', '', 'world456', 'hello789', '', 'world', 'hello123', 'hello123', 'hello123', 'hello123', 'hello123']), ['hello', '', 'world'])
