import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_repeated_word('hello world hello'), 'hello')
        self.assertEqual(first_repeated_word('one two one'), 'one')

    def test_edge_conditions(self):
        self.assertEqual(first_repeated_word(''), 'None')
        self.assertEqual(first_repeated_word('unique'), 'None')

    def test_complex_cases(self):
        self.assertEqual(first_repeated_word('a b c a'), 'a')
        self.assertEqual(first_repeated_word('1 2 3 1'), '1')
        self.assertEqual(first_repeated_word('apple orange apple'), 'apple')

    def test_invalid_inputs(self):
        self.assertEqual(first_repeated_word(1234), 'None')
        self.assertEqual(first_repeated_word(['hello', 'world', 'hello']), 'None')
