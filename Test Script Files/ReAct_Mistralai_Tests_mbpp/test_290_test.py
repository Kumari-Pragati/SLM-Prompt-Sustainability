import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_empty_list(self):
        """Test max_length with an empty list"""
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        """Test max_length with a list containing a single element"""
        for element in ['a', 1, (1, 2, 3), set([1, 2, 3]), frozenset([1, 2, 3]):
            self.assertEqual(max_length([element]), (len(element), element))

    def test_list_with_different_lengths(self):
        """Test max_length with a list containing elements of different lengths"""
        self.assertEqual(max_length(['abc', 'def', 'ghi']), (3, 'ghi'))

    def test_list_with_equal_max_length(self):
        """Test max_length with a list containing elements of equal length"""
        self.assertEqual(max_length(['aaa', 'bbb', 'ccc']), (3, 'ccc'))

    def test_list_with_negative_strings(self):
        """Test max_length with a list containing negative strings"""
        self.assertEqual(max_length(['-abc', '-def', '-ghi']), (3, '-ghi'))

    def test_list_with_empty_strings(self):
        """Test max_length with a list containing empty strings"""
        self.assertEqual(max_length(['', 'abc', 'def']), (0, ''))

    def test_list_with_none(self):
        """Test max_length with a list containing None"""
        self.assertEqual(max_length([None, 'abc', 'def']), (3, 'def'))

    def test_list_with_lists(self):
        """Test max_length with a list containing lists"""
        self.assertEqual(max_length([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]),
                         (3, ['g', 'h', 'i']))

    def test_list_with_tuples(self):
        """Test max_length with a list containing tuples"""
        self.assertEqual(max_length([('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]),
                         (3, ('g', 'h', 'i')))

    def test_list_with_sets(self):
        """Test max_length with a list containing sets"""
        self.assertEqual(max_length([{'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'}]),
                         (3, {'g', 'h', 'i'}))

    def test_list_with_frozensets(self):
        """Test max_length with a list containing frozensets"""
        self.assertEqual(max_length([frozenset({'a', 'b', 'c'}), frozenset({'d', 'e', 'f'}), frozenset({'g', 'h', 'i'})]),
                         (3, frozenset({'g', 'h', 'i'})))
