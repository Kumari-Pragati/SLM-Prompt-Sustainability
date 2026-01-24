import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['a']), ' a')

    def test_multiple_elements(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), ' a b c')

    def test_mixed_types(self):
        self.assertEqual(concatenate_elements(['a', 1, True]), ' a1True')

    def test_list_with_spaces(self):
        self.assertEqual(concatenate_elements(['a', ' ', 'b']), ' a b')

    def test_list_with_duplicates(self):
        self.assertEqual(concatenate_elements(['a', 'a', 'b']), ' aa b')

    def test_list_with_none(self):
        self.assertEqual(concatenate_elements(['a', None, 'b']), ' aNone b')

    def test_list_with_empty_string(self):
        self.assertEqual(concatenate_elements(['', 'a', 'b']), ' a b')
