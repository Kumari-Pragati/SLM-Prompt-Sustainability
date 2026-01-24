import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_empty_lists(self):
        """Test if function returns 0 for empty lists"""
        self.assertEqual(overlapping([], []), 0)

    def test_single_element_lists(self):
        """Test if function returns 0 for lists with a single element"""
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    def test_identical_lists(self):
        """Test if function correctly identifies overlapping lists"""
        self.assertEqual(overlapping([1, 2, 3], [3, 2, 1]), 1)
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 0)

    def test_lists_with_duplicates(self):
        """Test if function correctly identifies overlapping lists with duplicates"""
        self.assertEqual(overlapping([1, 1, 2, 3], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 3]), 1)

    def test_lists_with_different_lengths(self):
        """Test if function correctly handles lists of different lengths"""
        self.assertEqual(overlapping([1, 2, 3], [1, 2]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 4]), 0)

    def test_lists_with_negative_numbers(self):
        """Test if function correctly handles lists with negative numbers"""
        self.assertEqual(overlapping([1, -2, 3], [-1, 2, 3]), 1)

    def test_lists_with_non_integer_elements(self):
        """Test if function correctly handles lists with non-integer elements"""
        self.assertRaises(TypeError, overlapping, [1, 'two', 3], [1, 2, 3])
