import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_find_literals(self):
        pattern = 'fox'
        text = 'The quick brown fox jumps over the lazy dog.'
        self.assertEqual(find_literals(text, pattern), ('fox', 20, 23))

        pattern = 'cat'
        text = 'The cat is sleeping in the garden.'
        self.assertEqual(find_literals(text, pattern), ('cat', 10, 13))

        pattern = 'apple'
        text = 'I love to eat an apple.'
        self.assertEqual(find_literals(text, pattern), ('apple', 15, 20))

        pattern = 'banana'
        text = 'I do not like bananas.'
        self.assertEqual(find_literals(text, pattern), ('banana', 12, 18))
