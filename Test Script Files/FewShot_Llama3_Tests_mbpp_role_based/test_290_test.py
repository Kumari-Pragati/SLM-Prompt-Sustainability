import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length(['hello']), (5, 'hello'))

    def test_multiple_element_list(self):
        self.assertEqual(max_length(['hello', 'world', 'abc']), (6, 'world'))

    def test_list_with_empty_string(self):
        self.assertEqual(max_length(['hello', '', 'world']), (6, 'world'))

    def test_list_with_mixed_length_strings(self):
        self.assertEqual(max_length(['hello', 'world', 'abc','short']), (7, 'world'))

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            max_length([1, 'hello', 'world'])
