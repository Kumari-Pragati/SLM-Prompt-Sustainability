import unittest
from947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_item_list(self):
        for item in ['a', [1], (1,), 1.0, b'test', frozenset({1, 2, 3}), set([1, 2, 3]), dict({1: 'a'}), None]:
            self.assertEqual(len_log([item]), len(item))

    def test_multiple_items_with_same_length(self):
        self.assertEqual(len_log([list('abc'), list('def'), list('ghi'), [1, 2, 3]]), max(map(len, [list('abc'), list('def'), list('ghi'), [1, 2, 3]])))

    def test_multiple_items_with_different_lengths(self):
        self.assertEqual(len_log([list('abc'), list('def'), list('ghi'), [1, 2]]), min(map(len, [list('abc'), list('def'), list('ghi'), [1, 2]])))

    def test_empty_strings(self):
        self.assertEqual(len_log(['', ' ', '\t', '\n']), 0)

    def test_negative_list(self):
        with self.assertRaises(TypeError):
            len_log([-1, -2, -3])

    def test_list_of_lists(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), min(map(len, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])))

    def test_list_of_tuples(self):
        self.assertEqual(len_log([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), min(map(len, [(1, 2, 3), (4, 5, 6), (7, 8, 9)])))

    def test_list_of_floats(self):
        self.assertEqual(len_log([1.1, 2.2, 3.3]), 0)

    def test_list_of_sets(self):
        self.assertEqual(len_log([set([1, 2, 3]), set([4, 5, 6]), set([7, 8, 9])]), max(map(len, [set([1, 2, 3]), set([4, 5, 6]), set([7, 8, 9])])))

    def test_list_of_dictionaries(self):
        self.assertEqual(len_log([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]), max(map(len, [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}])))

    def test_list_of_none(self):
        self.assertEqual(len_log([None, None, None]), 0)
