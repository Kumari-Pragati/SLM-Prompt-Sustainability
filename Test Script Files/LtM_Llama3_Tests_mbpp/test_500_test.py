import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]),'')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['hello']),'hello')

    def test_multiple_elements(self):
        self.assertEqual(concatenate_elements(['hello', 'world']),'hello world')

    def test_empty_string(self):
        self.assertEqual(concatenate_elements(['']),'')

    def test_single_empty_string(self):
        self.assertEqual(concatenate_elements(['']),'')

    def test_multiple_empty_strings(self):
        self.assertEqual(concatenate_elements(['', '']),'')

    def test_long_string(self):
        self.assertEqual(concatenate_elements(['hello' * 100]), 'hello'+ 'hello'* 99)

    def test_mixed_types(self):
        self.assertEqual(concatenate_elements(['hello', 123, 'world']),'hello 123 world')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements([123, 'world'])
