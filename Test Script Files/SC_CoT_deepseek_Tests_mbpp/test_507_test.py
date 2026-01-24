import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), ['apple'])

    def test_edge_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_corner_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry', 'durian']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_invalid_input(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = 12345
        with self.assertRaises(TypeError):
            remove_words(list1, removewords)
