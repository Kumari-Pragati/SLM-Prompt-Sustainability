import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), ' ')

    def test_single_element_list(self):
        self.assertEqual(concatenate_elements(['hello']), ' hello')

    def test_multiple_element_list(self):
        self.assertEqual(concatenate_elements(['hello', 'world']), ' hello world')

    def test_duplicate_elements_list(self):
        self.assertEqual(concatenate_elements(['hello', 'hello']), ' hello hello')

    def test_numeric_elements_list(self):
        self.assertEqual(concatenate_elements([1, 2, 3]), '  1 2 3')
