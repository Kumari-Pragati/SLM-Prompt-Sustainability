import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), ' a b c')

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['hello']), ' hello')

    def test_with_spaces(self):
        self.assertEqual(concatenate_elements(['hello', 'world']), ' hello world')

    def test_with_numbers(self):
        self.assertEqual(concatenate_elements([1, 2, 3]), ' 1 2 3')

    def test_with_mixed_types(self):
        self.assertEqual(concatenate_elements(['a', 1, 'b', 2]), ' a 1 b 2')
