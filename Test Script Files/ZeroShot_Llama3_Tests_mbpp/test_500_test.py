import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_concatenate_elements(self):
        self.assertEqual(concatenate_elements(['apple', 'banana', 'cherry']), 'apple banana cherry')
        self.assertEqual(concatenate_elements(['hello', 'world']), 'hello world')
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), 'a b c')
        self.assertEqual(concatenate_elements(['1', '2', '3']), '1 2 3')
        self.assertEqual(concatenate_elements(['apple', 'banana']), 'apple banana')

    def test_concatenate_elements_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_concatenate_elements_single_element(self):
        self.assertEqual(concatenate_elements(['apple']), 'apple')
