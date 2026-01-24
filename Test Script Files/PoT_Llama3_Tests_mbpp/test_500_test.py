import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(['apple', 'banana', 'cherry']),'apple banana cherry')

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]),'')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['hello']),'hello')

    def test_multiple_spaces(self):
        self.assertEqual(concatenate_elements(['hello', 'world']),'hello world')

    def test_edge_case(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c', 'd', 'e']),'a b c d e')

    def test_trailing_spaces(self):
        self.assertEqual(concatenate_elements(['hello', 'world', '']),'hello world ')

    def test_leading_spaces(self):
        self.assertEqual(concatenate_elements([' ', 'hello', 'world']),' hello world')
