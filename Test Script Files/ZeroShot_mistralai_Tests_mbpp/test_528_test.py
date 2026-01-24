import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(TypeError, min_length, [])

    def test_single_element_list(self):
        self.assertEqual(min_length(['a']), (1, 'a'))

    def test_list_with_same_length(self):
        self.assertEqual(min_length(['aa', 'bb', 'cc']), (2, 'aa'))

    def test_list_with_different_lengths(self):
        self.assertEqual(min_length(['aa', 'ab', 'abc']), (2, 'aa'))

    def test_list_with_negative_strings(self):
        self.assertEqual(min_length(['aa', '-a', 'ab']), (2, '-a'))
