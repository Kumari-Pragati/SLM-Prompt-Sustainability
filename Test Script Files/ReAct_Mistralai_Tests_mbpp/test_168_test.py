import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_empty_list(self):
        """Test frequency of an empty list"""
        self.assertEqual(frequency([]), 0)

    def test_single_element(self):
        """Test frequency of a single element"""
        self.assertEqual(frequency([1]), 1)

    def test_multiple_elements(self):
        """Test frequency of multiple elements"""
        self.assertEqual(frequency([1, 1, 2, 1, 3]), 3)

    def test_duplicate_elements(self):
        """Test frequency of duplicate elements"""
        self.assertEqual(frequency([1, 1, 1, 2, 2, 2, 3]), 3)

    def test_non_existent_element(self):
        """Test frequency of a non-existent element"""
        self.assertEqual(frequency([1, 1, 2, 1, 3], 4), 0)

    def test_negative_number(self):
        """Test frequency of a negative number"""
        self.assertEqual(frequency([-1, -1, 1, 1, -2], -1), 2)

    def test_large_input(self):
        """Test frequency with a large input"""
        large_list = [i for i in range(1000)]
        self.assertEqual(frequency(large_list, 999), len(large_list) - 1)

    def test_empty_input(self):
        """Test frequency with an empty input"""
        self.assertRaises(TypeError, frequency, [], "x")

    def test_non_iterable_input(self):
        """Test frequency with a non-iterable input"""
        self.assertRaises(TypeError, frequency, "string", "x")
