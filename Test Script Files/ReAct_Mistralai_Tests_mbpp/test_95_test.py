import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_empty_list(self):
        """Test finding minimum length of an empty list"""
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        """Test finding minimum length of a list with a single element"""
        for element in ['a', 1, (1, 2, 3), [1, 2, 3], set([1, 2, 3]), frozenset([1, 2, 3]), None:
            self.assertEqual(Find_Min_Length([element]), len(element))

    def test_list_with_different_lengths(self):
        """Test finding minimum length of a list with elements of different lengths"""
        self.assertEqual(Find_Min_Length(['abc', 'def', 'ghi']), 3)

    def test_list_with_duplicate_elements(self):
        """Test finding minimum length of a list with duplicate elements"""
        self.assertEqual(Find_Min_Length(['a', 'a', 'b', 'b', 'c']), 1)

    def test_list_with_zero_length_elements(self):
        """Test finding minimum length of a list with zero-length elements"""
        self.assertEqual(Find_Min_Length(['', [], (), {}, set(), frozenset(), None]), 0)

    def test_list_with_negative_length_elements(self):
        """Test finding minimum length of a list with negative-length elements"""
        self.assertEqual(Find_Min_Length(['-1', '-2', '-3']), 1)

    def test_list_with_non_string_non_iterable_elements(self):
        """Test finding minimum length of a list with non-string non-iterable elements"""
        self.assertRaises(TypeError, Find_Min_Length, [123, 456])
