import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), ' a b c')

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['single']), ' single')

    def test_large_list(self):
        large_list = ['a'] * 1000
        expected = ' ' + ' '.join(large_list)
        self.assertEqual(concatenate_elements(large_list), expected)

    def test_string_with_spaces(self):
        self.assertEqual(concatenate_elements(['a b', 'c d']), ' a b c d')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements(123)
