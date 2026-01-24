import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_string_list(['hello']), ['olleh'])

    def test_multiple_elements_list(self):
        self.assertEqual(reverse_string_list(['hello', 'world', 'python']), ['olleh', 'dlrow', 'nohtyp'])

    def test_list_with_empty_string(self):
        self.assertEqual(reverse_string_list(['hello', '', 'world']), ['olleh', '', 'dlrow'])

    def test_list_with_empty_string_at_end(self):
        self.assertEqual(reverse_string_list(['hello', 'world', '']), ['olleh', 'dlrow', ''])

    def test_list_with_empty_string_at_start(self):
        self.assertEqual(reverse_string_list(['', 'world', 'hello']), ['', 'dlrow', 'olleh'])

    def test_list_with_empty_string_in_middle(self):
        self.assertEqual(reverse_string_list(['hello', '', 'world', 'python']), ['olleh', '', 'dlrow', 'nohtyp'])

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            reverse_string_list([1, 'hello', 'world', 'python'])
