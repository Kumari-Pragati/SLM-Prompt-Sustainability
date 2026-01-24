import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_char_frequency(self):
        self.assertEqual(char_frequency('abc'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(char_frequency('aabbcc'), {'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(char_frequency(''), {})
        self.assertEqual(char_frequency('aaaabbbcc'), {'a': 4, 'b': 3, 'c': 2})
        self.assertEqual(char_frequency('123456'), {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1})
