import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        """Test len_log with an empty list"""
        self.assertEqual(len_log([]), 0)

    def test_single_element_list(self):
        """Test len_log with a list containing a single element"""
        self.assertEqual(len_log(['a']), 1)

    def test_multiple_elements_same_length(self):
        """Test len_log with a list containing multiple elements of the same length"""
        self.assertEqual(len_log(['abc', 'def', 'ghi']), 3)

    def test_multiple_elements_different_lengths_min_length(self):
        """Test len_log with a list containing multiple elements of different lengths, where the minimum length is returned"""
        self.assertEqual(len_log(['abc', 'a', 'xyz']), 2)

    def test_multiple_elements_different_lengths_max_length(self):
        """Test len_log with a list containing multiple elements of different lengths, where the maximum length is returned"""
        self.assertEqual(len_log(['a', 'abc', 'xyz']), 3)

    def test_negative_list_elements(self):
        """Test len_log with a list containing negative string elements"""
        self.assertEqual(len_log(['abc', '-123', 'xyz']), 3)

    def test_list_with_non_string_elements(self):
        """Test len_log with a list containing non-string elements"""
        with self.assertRaises(TypeError):
            len_log([1, 2, 3])
