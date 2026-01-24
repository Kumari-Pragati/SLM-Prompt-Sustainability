import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_remove_words(self):
        self.assertEqual(remove_words(['apple', 'banana', 'cherry'], ['banana', 'cherry']), ['apple'])
        self.assertEqual(remove_words(['apple', 'banana', 'cherry'], ['apple']), ['banana', 'cherry'])
        self.assertEqual(remove_words(['apple', 'banana', 'cherry'], []), ['apple', 'banana', 'cherry'])
        self.assertEqual(remove_words([], ['apple']), [])
        self.assertEqual(remove_words([], []), [])
