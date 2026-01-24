import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_char_long("Hello world"), ['Hello', 'world'])
        self.assertEqual(find_char_long("Python is awesome"), ['Python', 'awesome'])

    def test_edge_conditions(self):
        self.assertEqual(find_char_long(""), [])
        self.assertEqual(find_char_long("a"), [])
        self.assertEqual(find_char_long("123456"), [])

    def test_boundary_conditions(self):
        self.assertEqual(find_char_long("1234"), [])
        self.assertEqual(find_char_long("a" * 4), ['aaaa'])
        self.assertEqual(find_char_long("a" * 5), ['a' * 5])

    def test_complex_cases(self):
        self.assertEqual(find_char_long("This is a test sentence with multiple words"), 
                         ['multiple', 'words'])
        self.assertEqual(find_char_long("Find these words: word1, word2, word3"), 
                         ['word1', 'word2', 'word3'])
