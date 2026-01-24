import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_element_list(self):
        self.assertEqual(len_log(['a']), 1)
        self.assertEqual(len_log(['\t']), 1)
        self.assertEqual(len_log(['\n']), 1)

    def test_list_of_strings(self):
        self.assertEqual(len_log(['hello', 'world', 'this', 'is', 'a', 'test']), 5)

    def test_list_of_numbers(self):
        self.assertEqual(len_log([1, 2, 3, 4, 5]), 1)

    def test_list_of_lists(self):
        self.assertEqual(len_log([['a', 'b'], ['c', 'd']]), 2)
        self.assertEqual(len_log([['a'], ['b', 'c']]), 2)

    def test_list_of_tuples(self):
        self.assertEqual(len_log(('a', 'b', 'c')), 1)
        self.assertEqual(len_log(('a', ('b', 'c'))), 2)

    def test_list_of_dictionaries(self):
        self.assertEqual(len_log([{'a': 1}, {'b': 2}]), 2)
        self.assertEqual(len_log([{'a': 1, 'b': 2}, {'a': 3}]), 3)

    def test_list_of_empty_strings(self):
        self.assertEqual(len_log(['', ' ', '\t', '\n']), 1)

    def test_list_of_invalid_inputs(self):
        self.assertRaises(TypeError, len_log, [1, 2, 3])
        self.assertRaises(TypeError, len_log, [(1, 2, 3)])
        self.assertRaises(TypeError, len_log, [{'a': 1, 'b': 2}, {'c': 3}])
