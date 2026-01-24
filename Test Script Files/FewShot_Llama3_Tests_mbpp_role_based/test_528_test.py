import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(min_length(['hello']), (5, 'hello'))

    def test_multiple_element_list(self):
        self.assertEqual(min_length(['hello', 'world', 'abc']), (3, 'abc'))

    def test_list_with_empty_string(self):
        self.assertEqual(min_length(['hello', '', 'world']), (0, ''))

    def test_list_with_mixed_lengths(self):
        self.assertEqual(min_length(['hello', 'world', 'abc','short']), (4,'short'))

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            min_length([1, 2, 3])
