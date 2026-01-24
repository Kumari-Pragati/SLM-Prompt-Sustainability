import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_repeated_word('hello world hello'), 'hello')

    def test_no_repeated_word(self):
        self.assertEqual(first_repeated_word('unique words'), 'None')

    def test_edge_case_single_word(self):
        self.assertEqual(first_repeated_word('single'), 'None')

    def test_boundary_case_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_special_case_repeated_word_at_end(self):
        self.assertEqual(first_repeated_word('first second third second'), 'second')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            first_repeated_word(1234)
