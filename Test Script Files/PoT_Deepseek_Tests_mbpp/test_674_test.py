import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplicate('hello world'), 'hello world')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_boundary_case_single_word(self):
        self.assertEqual(remove_duplicate('python'), 'python')

    def test_boundary_case_duplicate_words(self):
        self.assertEqual(remove_duplicate('hello hello'), 'hello')

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(remove_duplicate('hello   world'), 'hello world')

    def test_corner_case_duplicate_words_with_spaces(self):
        self.assertEqual(remove_duplicate('hello   hello'), 'hello')
