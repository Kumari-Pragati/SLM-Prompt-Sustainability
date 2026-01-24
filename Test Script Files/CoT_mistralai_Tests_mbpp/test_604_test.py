import unittest
from mbpp_604_code import str
from six.moves.range import range

class TestReverseWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_words(''), '')

    def test_single_word(self):
        for word in ['hello', 'world', 'Python']:
            self.assertEqual(reverse_words(word), word[::-1])

    def test_multiple_words(self):
        for words in ['hello world', 'Python unittest', '604 code challenge']:
            self.assertEqual(reverse_words(words), words.replace(' ', '').replace(' ', '')[::-1])

    def test_whitespace_only(self):
        self.assertEqual(reverse_words('   '), '   ')

    def test_punctuation_and_numbers(self):
        for words in ['hello, world! 123', 'Python 4.5.6', 'unittest.run()']:
            self.assertEqual(reverse_words(words), words.replace(' ', '').replace('.', '').replace('!', '').replace('(', '').replace(')', '').replace(',', '').replace(';', '').replace(':', '').replace('5', '5').replace('4', '4').replace('6', '6').replace('1', '1').replace('2', '2').replace('3', '3')[::-1])

    def test_invalid_input(self):
        self.assertRaises(TypeError, reverse_words, 123)
        self.assertRaises(TypeError, reverse_words, None)
        self.assertRaises(TypeError, reverse_words, [1, 2, 3])
