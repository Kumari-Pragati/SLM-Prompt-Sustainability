import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_common([]), [])

    def test_single_word(self):
        self.assertEqual(count_common(['apple']), [('apple', 1)])

    def test_multiple_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange']), [('apple', 2), ('banana', 1), ('orange', 1)])

    def test_four_or_more_unique_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'orange', 'grape','mango']), [('apple', 1), ('banana', 1), ('grape', 1), ('mango', 1)])

    def test_four_or_more_words_with_duplicates(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange', 'banana', 'grape','mango']), [('apple', 2), ('banana', 2), ('grape', 1), ('mango', 1)])

    def test_no_words(self):
        with self.assertRaises(TypeError):
            count_common(None)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            count_common('hello')
