import unittest
from mbpp_674_code import OrderedDict
from six.moves import range

from674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_single_word(self):
        for word in ['apple', 'banana', 'cherry']:
            self.assertEqual(remove_duplicate(word), word)

    def test_multiple_words(self):
        for words in [('apple apple', 'apple'), ('apple banana', 'apple banana'), ('apple banana cherry', 'apple banana cherry')]:
            self.assertEqual(remove_duplicate(words[0]), words[1])

    def test_whitespace_only(self):
        self.assertEqual(remove_duplicate('   '), '')

    def test_leading_trailing_whitespace(self):
        for word in ['apple', 'banana', 'cherry']:
            for side in [' ', '\t']:
                self.assertEqual(remove_duplicate(side + word + side), word)

    def test_case_insensitive(self):
        for words in [('Apple apple', 'apple'), ('Apple Banana', 'apple banana'), ('Apple BAnAnA', 'apple banana')]:
            self.assertEqual(remove_duplicate(words[0]), words[1])

    def test_order_preserved(self):
        for words in [('apple banana apple', 'apple banana'), ('banana apple', 'banana apple')]:
            self.assertEqual(remove_duplicate(words[0]), words[1])

    def test_duplicate_words_in_middle(self):
        for words in [('apple apple banana', 'apple banana'), ('apple banana apple', 'apple banana')]:
            self.assertEqual(remove_duplicate(words[0]), words[1])

    def test_long_string(self):
        long_string = ' '.join(['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry'])
        self.assertEqual(remove_duplicate(long_string), long_string)

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_duplicate, 123)
        self.assertRaises(TypeError, remove_duplicate, (1, 2, 3))
        self.assertRaises(TypeError, remove_duplicate, [1, 2, 3])
        self.assertRaises(TypeError, remove_duplicate, {'a': 1, 'b': 2})
        self.assertRaises(TypeError, remove_duplicate, None)
