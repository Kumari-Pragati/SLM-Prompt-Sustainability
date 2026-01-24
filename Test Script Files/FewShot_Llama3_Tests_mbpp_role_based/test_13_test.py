import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_common([]), [])

    def test_single_word(self):
        self.assertEqual(count_common(['apple']), [('apple', 1)])

    def test_multiple_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange']), [('apple', 2), ('banana', 1), ('orange', 1)])

    def test_duplicates(self):
        self.assertEqual(count_common(['apple', 'apple', 'apple', 'banana']), [('apple', 3), ('banana', 1)])

    def test_long_list(self):
        words = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana', 'orange', 'apple', 'banana', 'orange']
        self.assertEqual(count_common(words), [('apple', 4), ('banana', 3), ('orange', 3)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_common('not a list')
