import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_empty_list(self):
        """Test min_length with an empty list"""
        self.assertIsNone(min_length([]))

    def test_single_element_list(self):
        """Test min_length with a list containing a single element"""
        for element in ['a', 1, (1, 2, 3), set([1, 2, 3]), frozenset([1, 2, 3])]:
            self.assertEqual(min_length([element]), (1, element))

    def test_list_with_same_length(self):
        """Test min_length with a list containing elements of the same length"""
        self.assertEqual(min_length(['abc', 'def', 'ghi']), (3, 'abc'))

    def test_list_with_different_lengths(self):
        """Test min_length with a list containing elements of different lengths"""
        self.assertEqual(min_length(['abc', 'defg', 'h']), (3, 'abc'))

    def test_list_with_zero_length_elements(self):
        """Test min_length with a list containing elements of zero length"""
        self.assertEqual(min_length(['', 'abc', 'defg', 'h']), (2, 'abc'))

    def test_list_with_negative_length_elements(self):
        """Test min_length with a list containing elements of negative length"""
        self.assertEqual(min_length(['abc', '-1', '-2', '-3']), (3, 'abc'))

    def test_list_with_non_iterable_elements(self):
        """Test min_length with a list containing non-iterable elements"""
        with self.assertRaises(TypeError):
            min_length(['abc', 1, None])
