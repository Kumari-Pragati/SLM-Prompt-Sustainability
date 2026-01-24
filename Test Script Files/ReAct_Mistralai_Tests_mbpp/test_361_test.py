import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], remove_empty([]))

    def test_list_with_empty_strings(self):
        self.assertListEqual(['a', 'b', '', 'c', 'd', ''], remove_empty(['a', 'b', '', 'c', 'd', '']))

    def test_list_with_only_empty_strings(self):
        self.assertListEqual([], remove_empty(['', '', '']))

    def test_list_with_numbers(self):
        self.assertListEqual([1, 2, 3, 0], remove_empty([1, 2, 3, 0]))

    def test_list_with_none(self):
        self.assertListEqual([1, 2, 3], remove_empty([1, 2, 3, None]))

    def test_list_with_lists(self):
        self.assertListEqual([[1, 2, 3], [4, 5, 6]], remove_empty([[1, 2, 3], [], [4, 5, 6]]))

    def test_list_with_tuples(self):
        self.assertListEqual([(1, 2, 3), (4, 5, 6)], remove_empty([(1, 2, 3), (), (4, 5, 6)]))

    def test_list_with_dicts(self):
        self.assertListEqual([{'a': 1, 'b': 2}, {'c': 3}], remove_empty([{'a': 1, 'b': 2}, {}, {'c': 3}]))
