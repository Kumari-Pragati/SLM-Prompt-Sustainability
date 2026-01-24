import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_single_element_list(self):
        self.assertEqual(max_length_list(['hello']), (5, ['hello']))

    def test_multiple_element_list(self):
        self.assertEqual(max_length_list(['hello', 'world', 'abc']), (6, ['world']))

    def test_list_with_empty_string(self):
        self.assertEqual(max_length_list(['hello', '', 'world']), (6, ['world']))

    def test_list_with_mixed_lengths(self):
        self.assertEqual(max_length_list(['hello', 'world', 'abc','short']), (7, ['world']))

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            max_length_list([1, 2, 3])
