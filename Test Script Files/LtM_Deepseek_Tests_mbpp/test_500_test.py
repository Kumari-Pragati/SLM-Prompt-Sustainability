import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), ' a b c')

    def test_empty_input(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element_input(self):
        self.assertEqual(concatenate_elements(['hello']), ' hello')

    def test_whitespace_in_elements(self):
        self.assertEqual(concatenate_elements(['a', 'b b', 'c']), ' a b b c')

    def test_numeric_elements(self):
        self.assertEqual(concatenate_elements([1, 2, 3]), ' 1 2 3')

    def test_mixed_type_elements(self):
        self.assertEqual(concatenate_elements(['a', 2, 'c']), ' a 2 c')
