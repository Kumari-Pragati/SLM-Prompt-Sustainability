import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_tuplex([], 1), 0)

    def test_single_element_list(self):
        self.assertEqual(count_tuplex([1], 1), 1)
        self.assertEqual(count_tuplex([1], 2), 0)

    def test_multiple_elements_list(self):
        self.assertEqual(count_tuplex([1, 2, 1, 3, 1], 1), 3)
        self.assertEqual(count_tuplex([1, 2, 1, 3, 1], 2), 0)

    def test_list_with_duplicates(self):
        self.assertEqual(count_tuplex([1, 1, 2, 1, 2, 1], 1), 3)

    def test_list_with_none_type(self):
        self.assertRaises(TypeError, count_tuplex, [None], 1)

    def test_list_with_string_type(self):
        self.assertRaises(TypeError, count_tuplex, ['1'], 1)

    def test_list_with_dictionary_type(self):
        self.assertRaises(TypeError, count_tuplex, [{1: 'a'}, 1], 1)
