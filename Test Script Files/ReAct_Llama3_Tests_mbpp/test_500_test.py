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
        self.assertEqual(concatenate_elements(['', '']),' ')

    def test_mixed_types(self):
        self.assertEqual(concatenate_elements([1, 'two', 3.0]),'1 two 3.0')

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements('not a list')

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate_elements([1, 2, 3])
